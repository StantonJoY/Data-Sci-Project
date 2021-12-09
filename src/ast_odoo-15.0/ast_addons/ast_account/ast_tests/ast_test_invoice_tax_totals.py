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
        Import(
            names=[alias(name='json', asname=None)],
        ),
        ClassDef(
            name='TestTaxTotals',
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
                                    value=Name(id='cls', ctx=Load()),
                                    attr='tax_group1',
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
                                        slice=Constant(value='account.tax.group', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1', kind=None),
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
                                    attr='tax_group2',
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
                                        slice=Constant(value='account.tax.group', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='2', kind=None),
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
                                    attr='tax_group_sub1',
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
                                        slice=Constant(value='account.tax.group', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='preceding_subtotal', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='subtotals 1', kind=None),
                                            Constant(value='PRE GROUP 1', kind=None),
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
                                    attr='tax_group_sub2',
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
                                        slice=Constant(value='account.tax.group', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='preceding_subtotal', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='subtotals 2', kind=None),
                                            Constant(value='PRE GROUP 2', kind=None),
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
                                    attr='tax_group_sub3',
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
                                        slice=Constant(value='account.tax.group', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='preceding_subtotal', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='subtotals 3', kind=None),
                                            Constant(value='PRE GROUP 1', kind=None),
                                            Constant(value=5, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='assertTaxTotals',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='document', annotation=None, type_comment=None),
                            arg(arg='expected_values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='main_keys_to_ignore', ctx=Store())],
                            value=Set(
                                elts=[
                                    Constant(value='formatted_amount_total', kind=None),
                                    Constant(value='formatted_amount_untaxed', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='group_keys_to_ignore', ctx=Store())],
                            value=Set(
                                elts=[
                                    Constant(value='group_key', kind=None),
                                    Constant(value='formatted_tax_group_amount', kind=None),
                                    Constant(value='formatted_tax_group_base_amount', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='subtotals_keys_to_ignore', ctx=Store())],
                            value=Set(
                                elts=[Constant(value='formatted_amount', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='to_compare', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='json', ctx=Load()),
                                    attr='loads',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='document', ctx=Load()),
                                        attr='tax_totals_json',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='key', ctx=Store()),
                            iter=Name(id='main_keys_to_ignore', ctx=Load()),
                            body=[
                                Delete(
                                    targets=[
                                        Subscript(
                                            value=Name(id='to_compare', ctx=Load()),
                                            slice=Name(id='key', ctx=Load()),
                                            ctx=Del(),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='key', ctx=Store()),
                            iter=Name(id='group_keys_to_ignore', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='groups', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='to_compare', ctx=Load()),
                                                slice=Constant(value='groups_by_subtotal', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='values',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        For(
                                            target=Name(id='group', ctx=Store()),
                                            iter=Name(id='groups', ctx=Load()),
                                            body=[
                                                Delete(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='group', ctx=Load()),
                                                            slice=Name(id='key', ctx=Load()),
                                                            ctx=Del(),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='key', ctx=Store()),
                            iter=Name(id='subtotals_keys_to_ignore', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='subtotal', ctx=Store()),
                                    iter=Subscript(
                                        value=Name(id='to_compare', ctx=Load()),
                                        slice=Constant(value='subtotals', kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Delete(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='subtotal', ctx=Load()),
                                                    slice=Name(id='key', ctx=Load()),
                                                    ctx=Del(),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
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
                                    Name(id='to_compare', ctx=Load()),
                                    Name(id='expected_values', ctx=Load()),
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
                    name='_create_document_for_tax_totals_test',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='lines_data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Creates and returns a new record of a model defining a tax_totals_json\n        field and using the related widget.\n\n        By default, this function creates an invoice, but it is overridden in sale\n        and purchase to create respectively a sale.order or a purchase.order. This way,\n        we can test the invoice_tax_totals from both these models in the same way as\n        account.move's.\n\n        :param lines_data: a list of tuple (amount, taxes), where amount is a base amount,\n                           and taxes a recordset of account.tax objects corresponding\n                           to the taxes to apply on this amount. Each element of the list\n                           corresponds to a line of the document (invoice line, PO line, SO line).\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='invoice_lines_vals', ctx=Store())],
                            value=ListComp(
                                elt=Tuple(
                                    elts=[
                                        Constant(value=0, kind=None),
                                        Constant(value=0, kind=None),
                                        Dict(
                                            keys=[
                                                Constant(value='name', kind=None),
                                                Constant(value='account_id', kind=None),
                                                Constant(value='price_unit', kind=None),
                                                Constant(value='tax_ids', kind=None),
                                            ],
                                            values=[
                                                Constant(value='line', kind=None),
                                                Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='company_data',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='default_account_revenue', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                Name(id='amount', ctx=Load()),
                                                List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value=6, kind=None),
                                                                Constant(value=0, kind=None),
                                                                Attribute(
                                                                    value=Name(id='taxes', ctx=Load()),
                                                                    attr='ids',
                                                                    ctx=Load(),
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
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='amount', ctx=Store()),
                                                Name(id='taxes', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Name(id='lines_data', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.move', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='move_type', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='invoice_date', kind=None),
                                            Constant(value='invoice_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='out_invoice', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='partner_a',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='2019-01-01', kind=None),
                                            Name(id='invoice_lines_vals', ctx=Load()),
                                        ],
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
                    name='test_multiple_tax_lines',
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
                            targets=[Name(id='tax_10', ctx=Store())],
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
                                            Constant(value='tax_group_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='tax_10', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=10.0, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tax_group1',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
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
                            targets=[Name(id='tax_20', ctx=Store())],
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
                                            Constant(value='tax_group_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='tax_20', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=20.0, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tax_group2',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
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
                            targets=[Name(id='document', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_create_document_for_tax_totals_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=1000, kind=None),
                                                    BinOp(
                                                        left=Name(id='tax_10', ctx=Load()),
                                                        op=Add(),
                                                        right=Name(id='tax_20', ctx=Load()),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1000, kind=None),
                                                    Name(id='tax_10', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1000, kind=None),
                                                    Name(id='tax_20', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTaxTotals',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='document', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='amount_total', kind=None),
                                            Constant(value='amount_untaxed', kind=None),
                                            Constant(value='allow_tax_edition', kind=None),
                                            Constant(value='groups_by_subtotal', kind=None),
                                            Constant(value='subtotals', kind=None),
                                        ],
                                        values=[
                                            Constant(value=3600, kind=None),
                                            Constant(value=3000, kind=None),
                                            Constant(value=False, kind=None),
                                            Dict(
                                                keys=[Constant(value='Untaxed Amount', kind=None)],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='tax_group_name', kind=None),
                                                                    Constant(value='tax_group_amount', kind=None),
                                                                    Constant(value='tax_group_base_amount', kind=None),
                                                                    Constant(value='tax_group_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=200, kind=None),
                                                                    Constant(value=2000, kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='tax_group_name', kind=None),
                                                                    Constant(value='tax_group_amount', kind=None),
                                                                    Constant(value='tax_group_base_amount', kind=None),
                                                                    Constant(value='tax_group_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=400, kind=None),
                                                                    Constant(value=2000, kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='amount', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='Untaxed Amount', kind=None),
                                                            Constant(value=3000, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='tax_20', ctx=Load()),
                                    attr='tax_group_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='tax_group1',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='document', ctx=Load()),
                                    attr='invalidate_cache',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='tax_totals_json', kind=None)],
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
                                    attr='assertTaxTotals',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='document', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='amount_total', kind=None),
                                            Constant(value='amount_untaxed', kind=None),
                                            Constant(value='allow_tax_edition', kind=None),
                                            Constant(value='groups_by_subtotal', kind=None),
                                            Constant(value='subtotals', kind=None),
                                        ],
                                        values=[
                                            Constant(value=3600, kind=None),
                                            Constant(value=3000, kind=None),
                                            Constant(value=False, kind=None),
                                            Dict(
                                                keys=[Constant(value='Untaxed Amount', kind=None)],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='tax_group_name', kind=None),
                                                                    Constant(value='tax_group_amount', kind=None),
                                                                    Constant(value='tax_group_base_amount', kind=None),
                                                                    Constant(value='tax_group_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=600, kind=None),
                                                                    Constant(value=3000, kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='amount', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='Untaxed Amount', kind=None),
                                                            Constant(value=3000, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
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
                    name='test_zero_tax_lines',
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
                            targets=[Name(id='tax_0', ctx=Store())],
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
                                        ],
                                        values=[
                                            Constant(value='tax_0', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=0.0, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='document', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_create_document_for_tax_totals_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=1000, kind=None),
                                                    Name(id='tax_0', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTaxTotals',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='document', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='amount_total', kind=None),
                                            Constant(value='amount_untaxed', kind=None),
                                            Constant(value='allow_tax_edition', kind=None),
                                            Constant(value='groups_by_subtotal', kind=None),
                                            Constant(value='subtotals', kind=None),
                                        ],
                                        values=[
                                            Constant(value=1000, kind=None),
                                            Constant(value=1000, kind=None),
                                            Constant(value=False, kind=None),
                                            Dict(
                                                keys=[Constant(value='Untaxed Amount', kind=None)],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='tax_group_name', kind=None),
                                                                    Constant(value='tax_group_amount', kind=None),
                                                                    Constant(value='tax_group_base_amount', kind=None),
                                                                    Constant(value='tax_group_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='tax_0', ctx=Load()),
                                                                            attr='tax_group_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=1000, kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='tax_0', ctx=Load()),
                                                                            attr='tax_group_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='amount', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='Untaxed Amount', kind=None),
                                                            Constant(value=1000, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
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
                    name='test_tax_affect_base_1',
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
                            targets=[Name(id='tax_10', ctx=Store())],
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
                                            Constant(value='tax_group_id', kind=None),
                                            Constant(value='price_include', kind=None),
                                            Constant(value='include_base_amount', kind=None),
                                        ],
                                        values=[
                                            Constant(value='tax_10', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=10.0, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tax_group1',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=True, kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tax_20', ctx=Store())],
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
                                            Constant(value='tax_group_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='tax_20', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=20.0, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tax_group2',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
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
                            targets=[Name(id='document', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_create_document_for_tax_totals_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=1100, kind=None),
                                                    BinOp(
                                                        left=Name(id='tax_10', ctx=Load()),
                                                        op=Add(),
                                                        right=Name(id='tax_20', ctx=Load()),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1100, kind=None),
                                                    Name(id='tax_10', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1000, kind=None),
                                                    Name(id='tax_20', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTaxTotals',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='document', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='amount_total', kind=None),
                                            Constant(value='amount_untaxed', kind=None),
                                            Constant(value='allow_tax_edition', kind=None),
                                            Constant(value='groups_by_subtotal', kind=None),
                                            Constant(value='subtotals', kind=None),
                                        ],
                                        values=[
                                            Constant(value=3620, kind=None),
                                            Constant(value=3000, kind=None),
                                            Constant(value=False, kind=None),
                                            Dict(
                                                keys=[Constant(value='Untaxed Amount', kind=None)],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='tax_group_name', kind=None),
                                                                    Constant(value='tax_group_amount', kind=None),
                                                                    Constant(value='tax_group_base_amount', kind=None),
                                                                    Constant(value='tax_group_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=200, kind=None),
                                                                    Constant(value=2000, kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='tax_group_name', kind=None),
                                                                    Constant(value='tax_group_amount', kind=None),
                                                                    Constant(value='tax_group_base_amount', kind=None),
                                                                    Constant(value='tax_group_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=420, kind=None),
                                                                    Constant(value=2100, kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='amount', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='Untaxed Amount', kind=None),
                                                            Constant(value=3000, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='tax_20', ctx=Load()),
                                    attr='tax_group_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='tax_group1',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='document', ctx=Load()),
                                    attr='invalidate_cache',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='tax_totals_json', kind=None)],
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
                                    attr='assertTaxTotals',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='document', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='amount_total', kind=None),
                                            Constant(value='amount_untaxed', kind=None),
                                            Constant(value='allow_tax_edition', kind=None),
                                            Constant(value='groups_by_subtotal', kind=None),
                                            Constant(value='subtotals', kind=None),
                                        ],
                                        values=[
                                            Constant(value=3620, kind=None),
                                            Constant(value=3000, kind=None),
                                            Constant(value=False, kind=None),
                                            Dict(
                                                keys=[Constant(value='Untaxed Amount', kind=None)],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='tax_group_name', kind=None),
                                                                    Constant(value='tax_group_amount', kind=None),
                                                                    Constant(value='tax_group_base_amount', kind=None),
                                                                    Constant(value='tax_group_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=620, kind=None),
                                                                    Constant(value=3000, kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='amount', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='Untaxed Amount', kind=None),
                                                            Constant(value=3000, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
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
                    name='test_tax_affect_base_2',
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
                            targets=[Name(id='tax_10', ctx=Store())],
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
                                            Constant(value='tax_group_id', kind=None),
                                            Constant(value='include_base_amount', kind=None),
                                        ],
                                        values=[
                                            Constant(value='tax_10', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=10.0, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tax_group1',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tax_20', ctx=Store())],
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
                                            Constant(value='tax_group_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='tax_20', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=20.0, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tax_group1',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
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
                            targets=[Name(id='tax_30', ctx=Store())],
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
                                            Constant(value='tax_group_id', kind=None),
                                            Constant(value='include_base_amount', kind=None),
                                        ],
                                        values=[
                                            Constant(value='tax_30', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=30.0, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tax_group2',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='document', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_create_document_for_tax_totals_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=1000, kind=None),
                                                    BinOp(
                                                        left=Name(id='tax_10', ctx=Load()),
                                                        op=Add(),
                                                        right=Name(id='tax_20', ctx=Load()),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1000, kind=None),
                                                    BinOp(
                                                        left=Name(id='tax_30', ctx=Load()),
                                                        op=Add(),
                                                        right=Name(id='tax_10', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTaxTotals',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='document', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='amount_total', kind=None),
                                            Constant(value='amount_untaxed', kind=None),
                                            Constant(value='allow_tax_edition', kind=None),
                                            Constant(value='groups_by_subtotal', kind=None),
                                            Constant(value='subtotals', kind=None),
                                        ],
                                        values=[
                                            Constant(value=2750, kind=None),
                                            Constant(value=2000, kind=None),
                                            Constant(value=False, kind=None),
                                            Dict(
                                                keys=[Constant(value='Untaxed Amount', kind=None)],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='tax_group_name', kind=None),
                                                                    Constant(value='tax_group_amount', kind=None),
                                                                    Constant(value='tax_group_base_amount', kind=None),
                                                                    Constant(value='tax_group_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=450, kind=None),
                                                                    Constant(value=2300, kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='tax_group_name', kind=None),
                                                                    Constant(value='tax_group_amount', kind=None),
                                                                    Constant(value='tax_group_base_amount', kind=None),
                                                                    Constant(value='tax_group_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=300, kind=None),
                                                                    Constant(value=1000, kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='amount', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='Untaxed Amount', kind=None),
                                                            Constant(value=2000, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='tax_30', ctx=Load()),
                                    attr='tax_group_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='tax_group1',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='document', ctx=Load()),
                                    attr='invalidate_cache',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='tax_totals_json', kind=None)],
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
                                    attr='assertTaxTotals',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='document', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='amount_total', kind=None),
                                            Constant(value='amount_untaxed', kind=None),
                                            Constant(value='allow_tax_edition', kind=None),
                                            Constant(value='groups_by_subtotal', kind=None),
                                            Constant(value='subtotals', kind=None),
                                        ],
                                        values=[
                                            Constant(value=2750, kind=None),
                                            Constant(value=2000, kind=None),
                                            Constant(value=False, kind=None),
                                            Dict(
                                                keys=[Constant(value='Untaxed Amount', kind=None)],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='tax_group_name', kind=None),
                                                                    Constant(value='tax_group_amount', kind=None),
                                                                    Constant(value='tax_group_base_amount', kind=None),
                                                                    Constant(value='tax_group_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=750, kind=None),
                                                                    Constant(value=2000, kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='amount', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='Untaxed Amount', kind=None),
                                                            Constant(value=2000, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
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
                    name='test_subtotals_basic',
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
                            targets=[Name(id='tax_10', ctx=Store())],
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
                                            Constant(value='tax_group_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='tax_10', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=10.0, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tax_group_sub1',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
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
                            targets=[Name(id='tax_25', ctx=Store())],
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
                                            Constant(value='tax_group_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='tax_25', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=25.0, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tax_group_sub2',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
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
                            targets=[Name(id='tax_42', ctx=Store())],
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
                                            Constant(value='tax_group_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='tax_42', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=42.0, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tax_group1',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
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
                            targets=[Name(id='document', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_create_document_for_tax_totals_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=1000, kind=None),
                                                    Name(id='tax_10', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1000, kind=None),
                                                    Name(id='tax_25', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=100, kind=None),
                                                    Name(id='tax_42', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=200, kind=None),
                                                    BinOp(
                                                        left=BinOp(
                                                            left=Name(id='tax_42', ctx=Load()),
                                                            op=Add(),
                                                            right=Name(id='tax_10', ctx=Load()),
                                                        ),
                                                        op=Add(),
                                                        right=Name(id='tax_25', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTaxTotals',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='document', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='amount_total', kind=None),
                                            Constant(value='amount_untaxed', kind=None),
                                            Constant(value='allow_tax_edition', kind=None),
                                            Constant(value='groups_by_subtotal', kind=None),
                                            Constant(value='subtotals', kind=None),
                                        ],
                                        values=[
                                            Constant(value=2846, kind=None),
                                            Constant(value=2300, kind=None),
                                            Constant(value=False, kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='Untaxed Amount', kind=None),
                                                    Constant(value='PRE GROUP 1', kind=None),
                                                    Constant(value='PRE GROUP 2', kind=None),
                                                ],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='tax_group_name', kind=None),
                                                                    Constant(value='tax_group_amount', kind=None),
                                                                    Constant(value='tax_group_base_amount', kind=None),
                                                                    Constant(value='tax_group_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=126, kind=None),
                                                                    Constant(value=300, kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='tax_group_name', kind=None),
                                                                    Constant(value='tax_group_amount', kind=None),
                                                                    Constant(value='tax_group_base_amount', kind=None),
                                                                    Constant(value='tax_group_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group_sub1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=120, kind=None),
                                                                    Constant(value=1200, kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group_sub1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='tax_group_name', kind=None),
                                                                    Constant(value='tax_group_amount', kind=None),
                                                                    Constant(value='tax_group_base_amount', kind=None),
                                                                    Constant(value='tax_group_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group_sub2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=300, kind=None),
                                                                    Constant(value=1200, kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group_sub2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='amount', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='Untaxed Amount', kind=None),
                                                            Constant(value=2300, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='amount', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='PRE GROUP 1', kind=None),
                                                            Constant(value=2426, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='amount', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='PRE GROUP 2', kind=None),
                                                            Constant(value=2546, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
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
                    name='test_after_total_mix',
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
                            targets=[Name(id='tax_10', ctx=Store())],
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
                                            Constant(value='tax_group_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='tax_10', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=10.0, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tax_group_sub3',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
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
                            targets=[Name(id='tax_25', ctx=Store())],
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
                                            Constant(value='tax_group_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='tax_25', kind=None),
                                            Constant(value='percent', kind=None),
                                            UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=25.0, kind=None),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tax_group_sub2',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
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
                            targets=[Name(id='tax_42', ctx=Store())],
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
                                            Constant(value='tax_group_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='tax_42', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=42.0, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tax_group_sub1',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
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
                            targets=[Name(id='tax_30', ctx=Store())],
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
                                            Constant(value='tax_group_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='tax_30', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=30.0, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tax_group1',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
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
                            targets=[Name(id='document', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_create_document_for_tax_totals_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=100, kind=None),
                                                    Name(id='tax_10', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=100, kind=None),
                                                    BinOp(
                                                        left=BinOp(
                                                            left=Name(id='tax_25', ctx=Load()),
                                                            op=Add(),
                                                            right=Name(id='tax_42', ctx=Load()),
                                                        ),
                                                        op=Add(),
                                                        right=Name(id='tax_30', ctx=Load()),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=200, kind=None),
                                                    BinOp(
                                                        left=Name(id='tax_10', ctx=Load()),
                                                        op=Add(),
                                                        right=Name(id='tax_25', ctx=Load()),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1000, kind=None),
                                                    Name(id='tax_30', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=100, kind=None),
                                                    BinOp(
                                                        left=Name(id='tax_30', ctx=Load()),
                                                        op=Add(),
                                                        right=Name(id='tax_10', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTaxTotals',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='document', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='amount_total', kind=None),
                                            Constant(value='amount_untaxed', kind=None),
                                            Constant(value='allow_tax_edition', kind=None),
                                            Constant(value='groups_by_subtotal', kind=None),
                                            Constant(value='subtotals', kind=None),
                                        ],
                                        values=[
                                            Constant(value=1867, kind=None),
                                            Constant(value=1500, kind=None),
                                            Constant(value=False, kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='Untaxed Amount', kind=None),
                                                    Constant(value='PRE GROUP 1', kind=None),
                                                    Constant(value='PRE GROUP 2', kind=None),
                                                ],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='tax_group_name', kind=None),
                                                                    Constant(value='tax_group_amount', kind=None),
                                                                    Constant(value='tax_group_base_amount', kind=None),
                                                                    Constant(value='tax_group_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=360, kind=None),
                                                                    Constant(value=1200, kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='tax_group_name', kind=None),
                                                                    Constant(value='tax_group_amount', kind=None),
                                                                    Constant(value='tax_group_base_amount', kind=None),
                                                                    Constant(value='tax_group_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group_sub1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=42, kind=None),
                                                                    Constant(value=100, kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group_sub1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='tax_group_name', kind=None),
                                                                    Constant(value='tax_group_amount', kind=None),
                                                                    Constant(value='tax_group_base_amount', kind=None),
                                                                    Constant(value='tax_group_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group_sub3',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=40, kind=None),
                                                                    Constant(value=400, kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group_sub3',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='tax_group_name', kind=None),
                                                                    Constant(value='tax_group_amount', kind=None),
                                                                    Constant(value='tax_group_base_amount', kind=None),
                                                                    Constant(value='tax_group_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group_sub2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    UnaryOp(
                                                                        op=USub(),
                                                                        operand=Constant(value=75, kind=None),
                                                                    ),
                                                                    Constant(value=300, kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='tax_group_sub2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='amount', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='Untaxed Amount', kind=None),
                                                            Constant(value=1500, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='amount', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='PRE GROUP 1', kind=None),
                                                            Constant(value=1860, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='amount', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='PRE GROUP 2', kind=None),
                                                            Constant(value=1942, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
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
