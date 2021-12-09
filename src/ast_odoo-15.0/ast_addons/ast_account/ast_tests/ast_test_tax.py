Module(
    body=[
        ImportFrom(
            module='odoo.addons.account.tests.common',
            names=[alias(name='AccountTestInvoicingCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestTaxCommon',
            bases=[Name(id='AccountTestInvoicingCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUpClass',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='chart_template_ref', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='setUpClass',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='chart_template_ref',
                                        value=Name(id='chart_template_ref', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='currency_data',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='currency', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='rounding',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=1.0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='currency_no_decimal',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='currency_data',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='currency', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='company_data_2',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='setup_company_data',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='company_2', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='currency_id',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='currency_no_decimal',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                    attr='company_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='company_data',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='company', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='fixed_tax',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.tax', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Fixed tax', kind=None),
                                            Constant(value='fixed', kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='fixed_tax_bis',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.tax', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Fixed tax bis', kind=None),
                                            Constant(value='fixed', kind=None),
                                            Constant(value=15, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='percent_tax',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.tax', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Percent tax', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=3, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='percent_tax_bis',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.tax', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Percent tax bis', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=4, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='division_tax',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.tax', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Division tax', kind=None),
                                            Constant(value='division', kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=4, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='group_tax',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.tax', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='sequence', kind=None),
                                            Constant(value='children_tax_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Group tax', kind=None),
                                            Constant(value='group', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=5, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='cls', ctx=Load()),
                                                                    attr='fixed_tax',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='cls', ctx=Load()),
                                                                    attr='percent_tax',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='group_tax_bis',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.tax', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='sequence', kind=None),
                                            Constant(value='children_tax_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Group tax bis', kind=None),
                                            Constant(value='group', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=6, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='cls', ctx=Load()),
                                                                    attr='fixed_tax',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='cls', ctx=Load()),
                                                                    attr='percent_tax',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='group_tax_percent',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.tax', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='sequence', kind=None),
                                            Constant(value='children_tax_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Group tax percent', kind=None),
                                            Constant(value='group', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=6, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='cls', ctx=Load()),
                                                                    attr='percent_tax',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='cls', ctx=Load()),
                                                                    attr='percent_tax_bis',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='group_of_group_tax',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.tax', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='sequence', kind=None),
                                            Constant(value='children_tax_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Group of group tax', kind=None),
                                            Constant(value='group', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=7, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='cls', ctx=Load()),
                                                                    attr='group_tax',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='cls', ctx=Load()),
                                                                    attr='group_tax_bis',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='tax_with_no_account',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.tax', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Tax with no account', kind=None),
                                            Constant(value='fixed', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=8, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='some_account', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.account', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='tax_with_account',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.tax', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='sequence', kind=None),
                                            Constant(value='invoice_repartition_line_ids', kind=None),
                                            Constant(value='refund_repartition_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Tax with account', kind=None),
                                            Constant(value='fixed', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=8, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='factor_percent', kind=None),
                                                                    Constant(value='repartition_type', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value=100, kind=None),
                                                                    Constant(value='base', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='factor_percent', kind=None),
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value=100, kind=None),
                                                                    Constant(value='tax', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='some_account', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='factor_percent', kind=None),
                                                                    Constant(value='repartition_type', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value=100, kind=None),
                                                                    Constant(value='base', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='factor_percent', kind=None),
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value=100, kind=None),
                                                                    Constant(value='tax', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='some_account', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='tax_0_percent',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.tax', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_company',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='company_data',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='company', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_0_percent', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='tax_5_percent',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.tax', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_company',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='company_data',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='company', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_5_percent', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=5, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='tax_8_percent',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.tax', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_company',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='company_data',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='company', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_8_percent', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=8, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='tax_12_percent',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.tax', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_company',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='company_data',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='company', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_12_percent', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=12, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='tax_19_percent',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.tax', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_company',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='company_data_2',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='company', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_19_percent', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=19, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='tax_21_percent',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.tax', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_company',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='company_data',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='company', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_21_percent', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=19, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='tax_21_percent',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.tax', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_company',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='company_data',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='company', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_rounding_methods_2', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=21, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='bank_journal',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='company_data',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='default_journal_bank', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='bank_account',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='bank_journal',
                                    ctx=Load(),
                                ),
                                attr='default_account_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='expense_account',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='company_data',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='default_account_expense', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_compute_all_results',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='total_included', annotation=None, type_comment=None),
                            arg(arg='total_excluded', annotation=None, type_comment=None),
                            arg(arg='taxes', annotation=None, type_comment=None),
                            arg(arg='res', annotation=None, type_comment=None),
                        ],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertAlmostEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='res', ctx=Load()),
                                        slice=Constant(value='total_included', kind=None),
                                        ctx=Load(),
                                    ),
                                    Name(id='total_included', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertAlmostEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='res', ctx=Load()),
                                        slice=Constant(value='total_excluded', kind=None),
                                        ctx=Load(),
                                    ),
                                    Name(id='total_excluded', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='i', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[
                                    Constant(value=0, kind=None),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='taxes', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertAlmostEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='res', ctx=Load()),
                                                        slice=Constant(value='taxes', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='i', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='base', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Subscript(
                                                    value=Name(id='taxes', ctx=Load()),
                                                    slice=Name(id='i', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertAlmostEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='res', ctx=Load()),
                                                        slice=Constant(value='taxes', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='i', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Subscript(
                                                    value=Name(id='taxes', ctx=Load()),
                                                    slice=Name(id='i', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=1, kind=None),
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
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
        ClassDef(
            name='TestTax',
            bases=[Name(id='TestTaxCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUpClass',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='TestTax', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUpClass',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_tax_group_of_group_tax',
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
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='fixed_tax',
                                        ctx=Load(),
                                    ),
                                    attr='include_base_amount',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='group_of_group_tax',
                                        ctx=Load(),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=200.0, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=263, kind=None),
                                    Constant(value=200, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=200.0, kind=None),
                                                    Constant(value=10.0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=210.0, kind=None),
                                                    Constant(value=21.0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=210.0, kind=None),
                                                    Constant(value=10.0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=220.0, kind=None),
                                                    Constant(value=22.0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_tax_group',
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
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='group_tax',
                                        ctx=Load(),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=200.0, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=230, kind=None),
                                    Constant(value=200, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=200.0, kind=None),
                                                    Constant(value=10.0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=200.0, kind=None),
                                                    Constant(value=20.0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_tax_group_percent',
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
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='group_tax_percent',
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='force_price_include', kind=None)],
                                                values=[Constant(value=True, kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=100.0, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=100, kind=None),
                                    Constant(value=83.33, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=83.33, kind=None),
                                                    Constant(value=8.33, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=83.33, kind=None),
                                                    Constant(value=8.34, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_tax_percent_division',
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
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='division_tax',
                                        ctx=Load(),
                                    ),
                                    attr='price_include',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='division_tax',
                                        ctx=Load(),
                                    ),
                                    attr='include_base_amount',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res_division', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='division_tax',
                                        ctx=Load(),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=200.0, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=200, kind=None),
                                    Constant(value=180, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=180.0, kind=None),
                                                    Constant(value=20.0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res_division', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='percent_tax',
                                        ctx=Load(),
                                    ),
                                    attr='price_include',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='percent_tax',
                                        ctx=Load(),
                                    ),
                                    attr='include_base_amount',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res_percent', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='percent_tax',
                                        ctx=Load(),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=100.0, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=110, kind=None),
                                    Constant(value=100, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=100.0, kind=None),
                                                    Constant(value=10.0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res_percent', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='division_tax',
                                        ctx=Load(),
                                    ),
                                    attr='price_include',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='division_tax',
                                        ctx=Load(),
                                    ),
                                    attr='include_base_amount',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res_division', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='division_tax',
                                        ctx=Load(),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=180.0, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=200, kind=None),
                                    Constant(value=180, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=180.0, kind=None),
                                                    Constant(value=20.0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res_division', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='percent_tax',
                                        ctx=Load(),
                                    ),
                                    attr='price_include',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='percent_tax',
                                        ctx=Load(),
                                    ),
                                    attr='include_base_amount',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res_percent', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='percent_tax',
                                        ctx=Load(),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=110.0, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=110, kind=None),
                                    Constant(value=100, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=100.0, kind=None),
                                                    Constant(value=10.0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res_percent', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='percent_tax_bis',
                                        ctx=Load(),
                                    ),
                                    attr='price_include',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='percent_tax_bis',
                                        ctx=Load(),
                                    ),
                                    attr='include_base_amount',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='percent_tax_bis',
                                        ctx=Load(),
                                    ),
                                    attr='amount',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=21, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res_percent', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='percent_tax_bis',
                                        ctx=Load(),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=7.0, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=7.0, kind=None),
                                    Constant(value=5.79, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=5.79, kind=None),
                                                    Constant(value=1.21, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res_percent', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_tax_sequence_normalized_set',
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
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='division_tax',
                                        ctx=Load(),
                                    ),
                                    attr='sequence',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=1, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='fixed_tax',
                                        ctx=Load(),
                                    ),
                                    attr='sequence',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=2, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='percent_tax',
                                        ctx=Load(),
                                    ),
                                    attr='sequence',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=3, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='taxes_set', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='group_tax',
                                    ctx=Load(),
                                ),
                                op=BitOr(),
                                right=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='division_tax',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='taxes_set', ctx=Load()),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=200.0, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=252.22, kind=None),
                                    Constant(value=200, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=200.0, kind=None),
                                                    Constant(value=22.22, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=200.0, kind=None),
                                                    Constant(value=10.0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=200.0, kind=None),
                                                    Constant(value=20.0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_fixed_tax_include_base_amount',
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
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='fixed_tax',
                                        ctx=Load(),
                                    ),
                                    attr='include_base_amount',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='group_tax',
                                        ctx=Load(),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=200.0, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=231, kind=None),
                                    Constant(value=200, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=200.0, kind=None),
                                                    Constant(value=10.0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=210.0, kind=None),
                                                    Constant(value=21.0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='fixed_tax',
                                        ctx=Load(),
                                    ),
                                    attr='price_include',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='fixed_tax',
                                        ctx=Load(),
                                    ),
                                    attr='include_base_amount',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='fixed_tax',
                                        ctx=Load(),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=100.0, kind=None)],
                                keywords=[
                                    keyword(
                                        arg='quantity',
                                        value=Constant(value=2.0, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=200, kind=None),
                                    Constant(value=180, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=180.0, kind=None),
                                                    Constant(value=20.0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_percent_tax_include_base_amount',
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
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='percent_tax',
                                        ctx=Load(),
                                    ),
                                    attr='price_include',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='percent_tax',
                                        ctx=Load(),
                                    ),
                                    attr='amount',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=21.0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='percent_tax',
                                        ctx=Load(),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=7.0, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=7.0, kind=None),
                                    Constant(value=5.79, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=5.79, kind=None),
                                                    Constant(value=1.21, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='percent_tax',
                                        ctx=Load(),
                                    ),
                                    attr='price_include',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='percent_tax',
                                        ctx=Load(),
                                    ),
                                    attr='amount',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=20.0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='percent_tax',
                                        ctx=Load(),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=399.99, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=399.99, kind=None),
                                    Constant(value=333.33, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=333.33, kind=None),
                                                    Constant(value=66.66, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_tax_decimals',
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
                            value=Constant(value='Test the rounding of taxes up to 6 decimals (maximum decimals places allowed for currencies)', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                    attr='rounding',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=1e-06, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='percent_tax',
                                        ctx=Load(),
                                    ),
                                    attr='price_include',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='percent_tax',
                                        ctx=Load(),
                                    ),
                                    attr='amount',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=21.0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='percent_tax',
                                        ctx=Load(),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=7.0, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=7.0, kind=None),
                                    Constant(value=5.785124, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=5.785124, kind=None),
                                                    Constant(value=1.214876, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='percent_tax',
                                        ctx=Load(),
                                    ),
                                    attr='price_include',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='percent_tax',
                                        ctx=Load(),
                                    ),
                                    attr='amount',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=20.0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='percent_tax',
                                        ctx=Load(),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=399.999999, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=399.999999, kind=None),
                                    Constant(value=333.333333, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=333.333333, kind=None),
                                                    Constant(value=66.666666, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_advanced_taxes_computation_0',
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
                            value=Constant(value='Test more advanced taxes computation (see issue 34471).', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='tax_1', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='price_include', kind=None),
                                            Constant(value='include_base_amount', kind=None),
                                            Constant(value='sequence', kind=None),
                                            Constant(value='invoice_repartition_line_ids', kind=None),
                                            Constant(value='refund_repartition_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_advanced_taxes_computation_0_1', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=1, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='base', kind=None),
                                                                    Constant(value=100.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='base', kind=None),
                                                                    Constant(value=100.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tax_2', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='sequence', kind=None),
                                            Constant(value='invoice_repartition_line_ids', kind=None),
                                            Constant(value='refund_repartition_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_advanced_taxes_computation_0_2', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=2, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='base', kind=None),
                                                                    Constant(value=100.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='base', kind=None),
                                                                    Constant(value=100.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tax_3', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='price_include', kind=None),
                                            Constant(value='sequence', kind=None),
                                            Constant(value='invoice_repartition_line_ids', kind=None),
                                            Constant(value='refund_repartition_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_advanced_taxes_computation_0_3', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=3, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='base', kind=None),
                                                                    Constant(value=100.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='base', kind=None),
                                                                    Constant(value=100.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tax_4', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='sequence', kind=None),
                                            Constant(value='invoice_repartition_line_ids', kind=None),
                                            Constant(value='refund_repartition_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_advanced_taxes_computation_0_4', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=4, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='base', kind=None),
                                                                    Constant(value=100.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='base', kind=None),
                                                                    Constant(value=100.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tax_5', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='price_include', kind=None),
                                            Constant(value='sequence', kind=None),
                                            Constant(value='invoice_repartition_line_ids', kind=None),
                                            Constant(value='refund_repartition_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_advanced_taxes_computation_0_5', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=5, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='base', kind=None),
                                                                    Constant(value=100.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='base', kind=None),
                                                                    Constant(value=100.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='taxes', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=BinOp(
                                        left=BinOp(
                                            left=Name(id='tax_1', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='tax_2', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='tax_3', ctx=Load()),
                                    ),
                                    op=Add(),
                                    right=Name(id='tax_4', ctx=Load()),
                                ),
                                op=Add(),
                                right=Name(id='tax_5', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=154, kind=None),
                                    Constant(value=100, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=100.0, kind=None),
                                                    Constant(value=5.0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=100.0, kind=None),
                                                    Constant(value=5.0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=110.0, kind=None),
                                                    Constant(value=5.5, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=110.0, kind=None),
                                                    Constant(value=5.5, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=110.0, kind=None),
                                                    Constant(value=5.5, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=110.0, kind=None),
                                                    Constant(value=5.5, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=110.0, kind=None),
                                                    Constant(value=5.5, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=110.0, kind=None),
                                                    Constant(value=5.5, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=110.0, kind=None),
                                                    Constant(value=5.5, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=110.0, kind=None),
                                                    Constant(value=5.5, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='taxes', ctx=Load()),
                                            attr='compute_all',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=132.0, kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=154, kind=None),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=100, kind=None),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=100.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=5.0, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=100.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=5.0, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=110.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=5.5, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=110.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=5.5, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=110.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=5.5, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=110.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=5.5, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=110.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=5.5, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=110.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=5.5, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=110.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=5.5, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=110.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=5.5, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='taxes', ctx=Load()),
                                            attr='compute_all',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=132.0, kind=None),
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
                FunctionDef(
                    name='test_intracomm_taxes_computation_0',
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
                            value=Constant(value=' Test usage of intracomm taxes having e.g.+100%, -100% as repartition lines. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='intracomm_tax', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='invoice_repartition_line_ids', kind=None),
                                            Constant(value='refund_repartition_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_intracomm_taxes_computation_0_1', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=21, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='base', kind=None),
                                                                    Constant(value=100.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=100.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    UnaryOp(
                                                                        op=USub(),
                                                                        operand=Constant(value=100.0, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='base', kind=None),
                                                                    Constant(value=100.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=100.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    UnaryOp(
                                                                        op=USub(),
                                                                        operand=Constant(value=100.0, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=100, kind=None),
                                    Constant(value=100, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=100.0, kind=None),
                                                    Constant(value=21.0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=100.0, kind=None),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=21.0, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='intracomm_tax', ctx=Load()),
                                            attr='compute_all',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=100.0, kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=100, kind=None),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=100, kind=None),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=100.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=21.0, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=100.0, kind=None),
                                                    ),
                                                    Constant(value=21.0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='intracomm_tax', ctx=Load()),
                                            attr='compute_all',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=100.0, kind=None),
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
                FunctionDef(
                    name='test_rounding_issues_0',
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
                            value=Constant(value=' Test taxes having a complex setup of repartition lines. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='tax', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='invoice_repartition_line_ids', kind=None),
                                            Constant(value='refund_repartition_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_rounding_issues_0', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=3, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='base', kind=None),
                                                                    Constant(value=100.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='base', kind=None),
                                                                    Constant(value=100.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=1.09, kind=None),
                                    Constant(value=1, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=1.0, kind=None),
                                                    Constant(value=0.01, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1.0, kind=None),
                                                    Constant(value=0.01, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1.0, kind=None),
                                                    Constant(value=0.01, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1.0, kind=None),
                                                    Constant(value=0.02, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1.0, kind=None),
                                                    Constant(value=0.02, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1.0, kind=None),
                                                    Constant(value=0.02, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tax', ctx=Load()),
                                            attr='compute_all',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=1.0, kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1.09, kind=None),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=0.01, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=0.01, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=0.01, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=0.02, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=0.02, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=0.02, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tax', ctx=Load()),
                                            attr='compute_all',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1.0, kind=None),
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
                FunctionDef(
                    name='test_rounding_issues_1',
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
                            value=Constant(value=' Test taxes having a complex setup of repartition lines. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='tax', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='invoice_repartition_line_ids', kind=None),
                                            Constant(value='refund_repartition_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_advanced_taxes_repartition_lines_computation_1', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=3, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='base', kind=None),
                                                                    Constant(value=100.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    UnaryOp(
                                                                        op=USub(),
                                                                        operand=Constant(value=50.0, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=25.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=25.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    UnaryOp(
                                                                        op=USub(),
                                                                        operand=Constant(value=25.0, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    UnaryOp(
                                                                        op=USub(),
                                                                        operand=Constant(value=25.0, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='base', kind=None),
                                                                    Constant(value=100.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    UnaryOp(
                                                                        op=USub(),
                                                                        operand=Constant(value=50.0, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=25.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    Constant(value=25.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    UnaryOp(
                                                                        op=USub(),
                                                                        operand=Constant(value=25.0, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='repartition_type', kind=None),
                                                                    Constant(value='factor_percent', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax', kind=None),
                                                                    UnaryOp(
                                                                        op=USub(),
                                                                        operand=Constant(value=25.0, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=1, kind=None),
                                    Constant(value=1, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=1.0, kind=None),
                                                    Constant(value=0.02, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1.0, kind=None),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=0.02, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1.0, kind=None),
                                                    Constant(value=0.01, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1.0, kind=None),
                                                    Constant(value=0.01, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1.0, kind=None),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=0.01, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1.0, kind=None),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=0.01, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tax', ctx=Load()),
                                            attr='compute_all',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=1.0, kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=0.02, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1.0, kind=None),
                                                    ),
                                                    Constant(value=0.02, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=0.01, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=0.01, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1.0, kind=None),
                                                    ),
                                                    Constant(value=0.01, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1.0, kind=None),
                                                    ),
                                                    Constant(value=0.01, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tax', ctx=Load()),
                                            attr='compute_all',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1.0, kind=None),
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
                FunctionDef(
                    name='test_rounding_tax_excluded_round_per_line_01',
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
                            value=Constant(value=' Test the rounding of a 19% price excluded tax in an invoice having 22689 and 9176 as lines.\n        The decimal precision is set to zero.\n        The computation must be similar to round(22689 * 0.19) + round(9176 * 0.19).\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tax_19_percent',
                                                ctx=Load(),
                                            ),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                    attr='rounding',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=1.0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='tax_19_percent',
                                            ctx=Load(),
                                        ),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    attr='tax_calculation_rounding_method',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='round_per_line', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tax_19_percent',
                                        ctx=Load(),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=22689, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=27000, kind=None),
                                    Constant(value=22689, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=22689, kind=None),
                                                    Constant(value=4311, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res1', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tax_19_percent',
                                        ctx=Load(),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=9176, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=10919, kind=None),
                                    Constant(value=9176, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=9176, kind=None),
                                                    Constant(value=1743, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res2', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_rounding_tax_excluded_round_globally',
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
                            value=Constant(value=' Test the rounding of a 19% price excluded tax in an invoice having 22689 and 9176 as lines.\n        The decimal precision is set to zero.\n        The computation must be similar to round((22689 + 9176) * 0.19).\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='tax_19_percent',
                                            ctx=Load(),
                                        ),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    attr='tax_calculation_rounding_method',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='round_globally', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tax_19_percent',
                                        ctx=Load(),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=22689, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=27000, kind=None),
                                    Constant(value=22689, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=22689, kind=None),
                                                    Constant(value=4310.91, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res1', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tax_19_percent',
                                        ctx=Load(),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=9176, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=10919, kind=None),
                                    Constant(value=9176, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=9176, kind=None),
                                                    Constant(value=1743.44, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res2', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_rounding_tax_included_round_per_line_01',
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
                            value=Constant(value=' Test the rounding of a 19% price included tax in an invoice having 27000 and 10920 as lines.\n        The decimal precision is set to zero.\n        The computation must be similar to round(27000 / 1.19) + round(10920 / 1.19).\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tax_19_percent',
                                        ctx=Load(),
                                    ),
                                    attr='price_include',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tax_19_percent',
                                                ctx=Load(),
                                            ),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                    attr='rounding',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=1.0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='tax_19_percent',
                                            ctx=Load(),
                                        ),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    attr='tax_calculation_rounding_method',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='round_per_line', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tax_19_percent',
                                        ctx=Load(),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=27000, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=27000, kind=None),
                                    Constant(value=22689, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=22689, kind=None),
                                                    Constant(value=4311, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res1', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tax_19_percent',
                                        ctx=Load(),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=10920, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=10920, kind=None),
                                    Constant(value=9176, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=9176, kind=None),
                                                    Constant(value=1744, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res2', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_rounding_tax_included_round_per_line_02',
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
                            value=Constant(value=' Test the rounding of a 12% price included tax in an invoice having 52.50 as line.\n        The decimal precision is set to 2.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tax_12_percent',
                                        ctx=Load(),
                                    ),
                                    attr='price_include',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tax_12_percent',
                                                ctx=Load(),
                                            ),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                    attr='rounding',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=0.01, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tax_12_percent',
                                        ctx=Load(),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=52.5, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=52.5, kind=None),
                                    Constant(value=46.88, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=46.88, kind=None),
                                                    Constant(value=5.62, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res1', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_rounding_tax_included_round_per_line_03',
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
                            value=Constant(value=' Test the rounding of a 8% and 0% price included tax in an invoice having 8 * 15.55 as line.\n        The decimal precision is set to 2.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tax_0_percent',
                                                ctx=Load(),
                                            ),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                    attr='rounding',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=0.01, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tax_0_percent',
                                        ctx=Load(),
                                    ),
                                    attr='price_include',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tax_8_percent',
                                        ctx=Load(),
                                    ),
                                    attr='price_include',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='group_tax',
                                        ctx=Load(),
                                    ),
                                    attr='children_tax_ids',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value=6, kind=None),
                                            Constant(value=0, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tax_0_percent',
                                                    ctx=Load(),
                                                ),
                                                attr='ids',
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='group_tax_bis',
                                        ctx=Load(),
                                    ),
                                    attr='children_tax_ids',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value=6, kind=None),
                                            Constant(value=0, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tax_8_percent',
                                                    ctx=Load(),
                                                ),
                                                attr='ids',
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
                        Assign(
                            targets=[Name(id='res1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='tax_8_percent',
                                            ctx=Load(),
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='tax_0_percent',
                                            ctx=Load(),
                                        ),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=15.55, kind=None)],
                                keywords=[
                                    keyword(
                                        arg='quantity',
                                        value=Constant(value=8.0, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=124.4, kind=None),
                                    Constant(value=115.19, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=115.19, kind=None),
                                                    Constant(value=9.21, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=115.19, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res1', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='tax_0_percent',
                                            ctx=Load(),
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='tax_8_percent',
                                            ctx=Load(),
                                        ),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=15.55, kind=None)],
                                keywords=[
                                    keyword(
                                        arg='quantity',
                                        value=Constant(value=8.0, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=124.4, kind=None),
                                    Constant(value=115.19, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=115.19, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=115.19, kind=None),
                                                    Constant(value=9.21, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res2', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_rounding_tax_included_round_per_line_04',
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
                            value=Constant(value=' Test the rounding of a 5% price included tax.\n        The decimal precision is set to 0.05.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tax_5_percent',
                                        ctx=Load(),
                                    ),
                                    attr='price_include',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tax_5_percent',
                                                ctx=Load(),
                                            ),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                    attr='rounding',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=0.05, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='tax_5_percent',
                                            ctx=Load(),
                                        ),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    attr='tax_calculation_rounding_method',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='round_per_line', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tax_5_percent',
                                        ctx=Load(),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=5, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=5, kind=None),
                                    Constant(value=4.75, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=4.75, kind=None),
                                                    Constant(value=0.25, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res1', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tax_5_percent',
                                        ctx=Load(),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=10, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=10, kind=None),
                                    Constant(value=9.5, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=9.5, kind=None),
                                                    Constant(value=0.5, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res2', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res3', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tax_5_percent',
                                        ctx=Load(),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=50, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=50, kind=None),
                                    Constant(value=47.6, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=47.6, kind=None),
                                                    Constant(value=2.4, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res3', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_rounding_tax_included_round_globally_01',
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
                            value=Constant(value=' Test the rounding of a 19% price included tax in an invoice having 27000 and 10920 as lines.\n        The decimal precision is set to zero.\n        The computation must be similar to round((27000 + 10920) / 1.19).\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tax_19_percent',
                                        ctx=Load(),
                                    ),
                                    attr='price_include',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='tax_19_percent',
                                            ctx=Load(),
                                        ),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    attr='tax_calculation_rounding_method',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='round_globally', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tax_19_percent',
                                        ctx=Load(),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=27000, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=27000, kind=None),
                                    Constant(value=22689, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=22689, kind=None),
                                                    Constant(value=4311, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res1', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tax_19_percent',
                                        ctx=Load(),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=10920, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=10920, kind=None),
                                    Constant(value=9176, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=9176, kind=None),
                                                    Constant(value=1744, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res2', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_rounding_tax_included_round_globally_02',
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
                            value=Constant(value=' Test the rounding of a 21% price included tax in an invoice having 11.90 and 2.80 as lines.\n        The decimal precision is set to 2.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tax_21_percent',
                                        ctx=Load(),
                                    ),
                                    attr='price_include',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tax_21_percent',
                                                ctx=Load(),
                                            ),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                    attr='rounding',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=0.01, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='tax_21_percent',
                                            ctx=Load(),
                                        ),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    attr='tax_calculation_rounding_method',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='round_globally', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tax_21_percent',
                                        ctx=Load(),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=11.9, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=11.9, kind=None),
                                    Constant(value=9.83, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=9.83, kind=None),
                                                    Constant(value=2.07, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res1', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tax_21_percent',
                                        ctx=Load(),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=2.8, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=2.8, kind=None),
                                    Constant(value=2.31, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=2.31, kind=None),
                                                    Constant(value=0.49, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res2', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_rounding_tax_included_round_globally_03',
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
                            value=Constant(value=' Test the rounding of a 5% price included tax.\n        The decimal precision is set to 0.05.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tax_5_percent',
                                        ctx=Load(),
                                    ),
                                    attr='price_include',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tax_5_percent',
                                                ctx=Load(),
                                            ),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                    attr='rounding',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=0.05, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='tax_5_percent',
                                            ctx=Load(),
                                        ),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    attr='tax_calculation_rounding_method',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='round_globally', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tax_5_percent',
                                        ctx=Load(),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=5, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=5, kind=None),
                                    Constant(value=4.75, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=4.75, kind=None),
                                                    Constant(value=0.25, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res1', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tax_5_percent',
                                        ctx=Load(),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=10, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=10, kind=None),
                                    Constant(value=9.5, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=9.5, kind=None),
                                                    Constant(value=0.5, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res2', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res3', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tax_5_percent',
                                        ctx=Load(),
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=50, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=50, kind=None),
                                    Constant(value=47.6, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=47.6, kind=None),
                                                    Constant(value=2.4, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='res3', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_is_base_affected',
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
                            targets=[Name(id='taxes', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='name', kind=None),
                                                Constant(value='amount_type', kind=None),
                                                Constant(value='amount', kind=None),
                                                Constant(value='include_base_amount', kind=None),
                                                Constant(value='is_base_affected', kind=None),
                                                Constant(value='sequence', kind=None),
                                            ],
                                            values=[
                                                BinOp(
                                                    left=Constant(value='test_is_base_affected%s', kind=None),
                                                    op=Mod(),
                                                    right=Name(id='i', ctx=Load()),
                                                ),
                                                Constant(value='percent', kind=None),
                                                Name(id='amount', ctx=Load()),
                                                Name(id='include_base_amount', ctx=Load()),
                                                Name(id='is_base_affected', ctx=Load()),
                                                Name(id='i', ctx=Load()),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='i', ctx=Store()),
                                                        Name(id='amount', ctx=Store()),
                                                        Name(id='include_base_amount', ctx=Store()),
                                                        Name(id='is_base_affected', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value=0, kind=None),
                                                                Constant(value=6, kind=None),
                                                                Constant(value=True, kind=None),
                                                                Constant(value=True, kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        Tuple(
                                                            elts=[
                                                                Constant(value=1, kind=None),
                                                                Constant(value=6, kind=None),
                                                                Constant(value=True, kind=None),
                                                                Constant(value=False, kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        Tuple(
                                                            elts=[
                                                                Constant(value=2, kind=None),
                                                                Constant(value=10, kind=None),
                                                                Constant(value=False, kind=None),
                                                                Constant(value=True, kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
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
                        Assign(
                            targets=[Name(id='compute_all_results', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='taxes', ctx=Load()),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=100.0, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=123.2, kind=None),
                                    Constant(value=100.0, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=100.0, kind=None),
                                                    Constant(value=6.0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=100.0, kind=None),
                                                    Constant(value=6.0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=112.0, kind=None),
                                                    Constant(value=11.2, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='compute_all_results', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='expected_tax_ids_list', ctx=Store())],
                            value=List(
                                elts=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='taxes', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='taxes', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tax_ids_list', ctx=Store())],
                            value=ListComp(
                                elt=Subscript(
                                    value=Name(id='tax_line', ctx=Load()),
                                    slice=Constant(value='tax_ids', kind=None),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='tax_line', ctx=Store()),
                                        iter=Subscript(
                                            value=Name(id='compute_all_results', ctx=Load()),
                                            slice=Constant(value='taxes', kind=None),
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='tax_ids_list', ctx=Load()),
                                    Name(id='expected_tax_ids_list', ctx=Load()),
                                    Constant(value="Only a tax affected by previous taxes should have tax_ids set on its tax line when used after an 'include_base_amount' tax.", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_mixing_price_included_excluded_with_affect_base',
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
                            targets=[Name(id='tax_10_fix', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='include_base_amount', kind=None),
                                        ],
                                        values=[
                                            Constant(value='tax_10_fix', kind=None),
                                            Constant(value='fixed', kind=None),
                                            Constant(value=10.0, kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tax_21', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='price_include', kind=None),
                                            Constant(value='include_base_amount', kind=None),
                                        ],
                                        values=[
                                            Constant(value='tax_21', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=21.0, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=True, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_compute_all_results',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=1222.1, kind=None),
                                    Constant(value=1000.0, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=1000.0, kind=None),
                                                    Constant(value=10.0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1010.0, kind=None),
                                                    Constant(value=212.1, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=BinOp(
                                                left=Name(id='tax_10_fix', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='tax_21', ctx=Load()),
                                            ),
                                            attr='compute_all',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=1210, kind=None)],
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
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
