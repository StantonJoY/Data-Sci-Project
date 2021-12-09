Module(
    body=[
        ImportFrom(
            module='freezegun',
            names=[alias(name='freeze_time', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.account.tests.common',
            names=[alias(name='AccountTestInvoicingCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='Form', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='Command', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[
                alias(name='UserError', asname=None),
                alias(name='ValidationError', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='TestAccountMoveInInvoiceOnchanges',
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
                                    attr='invoice',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='init_invoice',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='in_invoice', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='products',
                                        value=BinOp(
                                            left=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='product_a',
                                                ctx=Load(),
                                            ),
                                            op=Add(),
                                            right=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='product_b',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='product_line_vals_1',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='product_id', kind=None),
                                    Constant(value='account_id', kind=None),
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='product_uom_id', kind=None),
                                    Constant(value='quantity', kind=None),
                                    Constant(value='discount', kind=None),
                                    Constant(value='price_unit', kind=None),
                                    Constant(value='price_subtotal', kind=None),
                                    Constant(value='price_total', kind=None),
                                    Constant(value='tax_ids', kind=None),
                                    Constant(value='tax_line_id', kind=None),
                                    Constant(value='currency_id', kind=None),
                                    Constant(value='amount_currency', kind=None),
                                    Constant(value='debit', kind=None),
                                    Constant(value='credit', kind=None),
                                    Constant(value='date_maturity', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='product_a',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='product_a',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='product_a',
                                                ctx=Load(),
                                            ),
                                            attr='property_account_expense_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='partner_a',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='product_a',
                                                ctx=Load(),
                                            ),
                                            attr='uom_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.0, kind=None),
                                    Constant(value=0.0, kind=None),
                                    Constant(value=800.0, kind=None),
                                    Constant(value=800.0, kind=None),
                                    Constant(value=920.0, kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='product_a',
                                                ctx=Load(),
                                            ),
                                            attr='supplier_taxes_id',
                                            ctx=Load(),
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='company_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='currency', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value=800.0, kind=None),
                                    Constant(value=800.0, kind=None),
                                    Constant(value=0.0, kind=None),
                                    Constant(value=False, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='product_line_vals_2',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='product_id', kind=None),
                                    Constant(value='account_id', kind=None),
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='product_uom_id', kind=None),
                                    Constant(value='quantity', kind=None),
                                    Constant(value='discount', kind=None),
                                    Constant(value='price_unit', kind=None),
                                    Constant(value='price_subtotal', kind=None),
                                    Constant(value='price_total', kind=None),
                                    Constant(value='tax_ids', kind=None),
                                    Constant(value='tax_line_id', kind=None),
                                    Constant(value='currency_id', kind=None),
                                    Constant(value='amount_currency', kind=None),
                                    Constant(value='debit', kind=None),
                                    Constant(value='credit', kind=None),
                                    Constant(value='date_maturity', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='product_b',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='product_b',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='product_b',
                                                ctx=Load(),
                                            ),
                                            attr='property_account_expense_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='partner_a',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='product_b',
                                                ctx=Load(),
                                            ),
                                            attr='uom_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.0, kind=None),
                                    Constant(value=0.0, kind=None),
                                    Constant(value=160.0, kind=None),
                                    Constant(value=160.0, kind=None),
                                    Constant(value=208.0, kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='product_b',
                                                ctx=Load(),
                                            ),
                                            attr='supplier_taxes_id',
                                            ctx=Load(),
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='company_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='currency', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value=160.0, kind=None),
                                    Constant(value=160.0, kind=None),
                                    Constant(value=0.0, kind=None),
                                    Constant(value=False, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='tax_line_vals_1',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='product_id', kind=None),
                                    Constant(value='account_id', kind=None),
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='product_uom_id', kind=None),
                                    Constant(value='quantity', kind=None),
                                    Constant(value='discount', kind=None),
                                    Constant(value='price_unit', kind=None),
                                    Constant(value='price_subtotal', kind=None),
                                    Constant(value='price_total', kind=None),
                                    Constant(value='tax_ids', kind=None),
                                    Constant(value='tax_line_id', kind=None),
                                    Constant(value='currency_id', kind=None),
                                    Constant(value='amount_currency', kind=None),
                                    Constant(value='debit', kind=None),
                                    Constant(value='credit', kind=None),
                                    Constant(value='date_maturity', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='tax_purchase_a',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='company_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='default_account_tax_purchase', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='partner_a',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                    Constant(value=1.0, kind=None),
                                    Constant(value=0.0, kind=None),
                                    Constant(value=144.0, kind=None),
                                    Constant(value=144.0, kind=None),
                                    Constant(value=144.0, kind=None),
                                    List(elts=[], ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='tax_purchase_a',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='company_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='currency', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value=144.0, kind=None),
                                    Constant(value=144.0, kind=None),
                                    Constant(value=0.0, kind=None),
                                    Constant(value=False, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='tax_line_vals_2',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='product_id', kind=None),
                                    Constant(value='account_id', kind=None),
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='product_uom_id', kind=None),
                                    Constant(value='quantity', kind=None),
                                    Constant(value='discount', kind=None),
                                    Constant(value='price_unit', kind=None),
                                    Constant(value='price_subtotal', kind=None),
                                    Constant(value='price_total', kind=None),
                                    Constant(value='tax_ids', kind=None),
                                    Constant(value='tax_line_id', kind=None),
                                    Constant(value='currency_id', kind=None),
                                    Constant(value='amount_currency', kind=None),
                                    Constant(value='debit', kind=None),
                                    Constant(value='credit', kind=None),
                                    Constant(value='date_maturity', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='tax_purchase_b',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='company_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='default_account_tax_purchase', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='partner_a',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                    Constant(value=1.0, kind=None),
                                    Constant(value=0.0, kind=None),
                                    Constant(value=24.0, kind=None),
                                    Constant(value=24.0, kind=None),
                                    Constant(value=24.0, kind=None),
                                    List(elts=[], ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='tax_purchase_b',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='company_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='currency', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value=24.0, kind=None),
                                    Constant(value=24.0, kind=None),
                                    Constant(value=0.0, kind=None),
                                    Constant(value=False, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='term_line_vals_1',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='product_id', kind=None),
                                    Constant(value='account_id', kind=None),
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='product_uom_id', kind=None),
                                    Constant(value='quantity', kind=None),
                                    Constant(value='discount', kind=None),
                                    Constant(value='price_unit', kind=None),
                                    Constant(value='price_subtotal', kind=None),
                                    Constant(value='price_total', kind=None),
                                    Constant(value='tax_ids', kind=None),
                                    Constant(value='tax_line_id', kind=None),
                                    Constant(value='currency_id', kind=None),
                                    Constant(value='amount_currency', kind=None),
                                    Constant(value='debit', kind=None),
                                    Constant(value='credit', kind=None),
                                    Constant(value='date_maturity', kind=None),
                                ],
                                values=[
                                    Constant(value='', kind=None),
                                    Constant(value=False, kind=None),
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='company_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='default_account_payable', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='partner_a',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                    Constant(value=1.0, kind=None),
                                    Constant(value=0.0, kind=None),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1128.0, kind=None),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1128.0, kind=None),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1128.0, kind=None),
                                    ),
                                    List(elts=[], ctx=Load()),
                                    Constant(value=False, kind=None),
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='company_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='currency', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1128.0, kind=None),
                                    ),
                                    Constant(value=0.0, kind=None),
                                    Constant(value=1128.0, kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Date',
                                                ctx=Load(),
                                            ),
                                            attr='from_string',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='2019-01-01', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='move_vals',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='currency_id', kind=None),
                                    Constant(value='journal_id', kind=None),
                                    Constant(value='date', kind=None),
                                    Constant(value='fiscal_position_id', kind=None),
                                    Constant(value='payment_reference', kind=None),
                                    Constant(value='invoice_payment_term_id', kind=None),
                                    Constant(value='amount_untaxed', kind=None),
                                    Constant(value='amount_tax', kind=None),
                                    Constant(value='amount_total', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='partner_a',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='company_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='currency', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='company_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='default_journal_purchase', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Date',
                                                ctx=Load(),
                                            ),
                                            attr='from_string',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='2019-01-01', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value=False, kind=None),
                                    Constant(value='', kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='pay_terms_a',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value=960.0, kind=None),
                                    Constant(value=168.0, kind=None),
                                    Constant(value=1128.0, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='setUp',
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='TestAccountMoveInInvoiceOnchanges', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUp',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertInvoiceValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_line_vals_1',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_line_vals_2',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tax_line_vals_1',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tax_line_vals_2',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='term_line_vals_1',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='move_vals',
                                        ctx=Load(),
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
                    name='test_in_invoice_onchange_invoice_date',
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
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='tax_date', ctx=Store()),
                                    Name(id='invoice_date', ctx=Store()),
                                    Name(id='accounting_date', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='2019-03-31', kind=None),
                                            Constant(value='2019-05-12', kind=None),
                                            Constant(value='2019-05-31', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='2019-03-31', kind=None),
                                            Constant(value='2019-02-10', kind=None),
                                            Constant(value='2019-04-30', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='2019-05-31', kind=None),
                                            Constant(value='2019-06-15', kind=None),
                                            Constant(value='2019-06-30', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='invoice',
                                                    ctx=Load(),
                                                ),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='tax_lock_date',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='tax_date', ctx=Load()),
                                    type_comment=None,
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='Form', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='invoice',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='move_form', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='move_form', ctx=Load()),
                                                    attr='invoice_date',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='invoice_date', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
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
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='invoice',
                                                    ctx=Load(),
                                                ),
                                                attr='date',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='to_date',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='accounting_date', ctx=Load())],
                                                keywords=[],
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
                FunctionDef(
                    name='test_in_invoice_onchange_invoice_date_2',
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
                            targets=[Name(id='invoice_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Call(
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
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='default_move_type',
                                                value=Constant(value='in_invoice', kind=None),
                                            ),
                                            keyword(
                                                arg='account_predictive_bills_disable_prediction',
                                                value=Constant(value=True, kind=None),
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
                                    value=Name(id='invoice_form', ctx=Load()),
                                    attr='partner_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='partner_a',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='invoice_form', ctx=Load()),
                                    attr='invoice_payment_term_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='account.account_payment_term_30days', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='invoice_form', ctx=Load()),
                                                attr='invoice_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='product_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_a',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='invoice_form', ctx=Load()),
                                    attr='invoice_date',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Date',
                                        ctx=Load(),
                                    ),
                                    attr='from_string',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='2021-09-01', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='invoice_form', ctx=Load()),
                                    attr='save',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='invoice', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='date', kind=None),
                                                    Constant(value='invoice_date', kind=None),
                                                    Constant(value='invoice_date_due', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='fields', ctx=Load()),
                                                                attr='Date',
                                                                ctx=Load(),
                                                            ),
                                                            attr='from_string',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='2021-09-16', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='fields', ctx=Load()),
                                                                attr='Date',
                                                                ctx=Load(),
                                                            ),
                                                            attr='from_string',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='2021-09-01', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='fields', ctx=Load()),
                                                                attr='Date',
                                                                ctx=Load(),
                                                            ),
                                                            attr='from_string',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='2021-10-01', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='freeze_time', ctx=Load()),
                            args=[Constant(value='2021-09-16', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_in_invoice_line_onchange_product_1',
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
                            targets=[Name(id='move_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='move_form', ctx=Load()),
                                                attr='invoice_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='edit',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=0, kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='product_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_b',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertInvoiceValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='name', kind=None),
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='product_uom_id', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='tax_ids', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='product_b',
                                                            ctx=Load(),
                                                        ),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='product_b',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_b',
                                                                ctx=Load(),
                                                            ),
                                                            attr='uom_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_b',
                                                                ctx=Load(),
                                                            ),
                                                            attr='property_account_expense_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=160.0, kind=None),
                                                    Constant(value=160.0, kind=None),
                                                    Constant(value=208.0, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_b',
                                                                ctx=Load(),
                                                            ),
                                                            attr='supplier_taxes_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=160.0, kind=None),
                                                    Constant(value=160.0, kind=None),
                                                ],
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_line_vals_2',
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=48.0, kind=None),
                                                    Constant(value=48.0, kind=None),
                                                    Constant(value=48.0, kind=None),
                                                    Constant(value=48.0, kind=None),
                                                    Constant(value=48.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=48.0, kind=None),
                                                    Constant(value=48.0, kind=None),
                                                    Constant(value=48.0, kind=None),
                                                    Constant(value=48.0, kind=None),
                                                    Constant(value=48.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='term_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=416.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=416.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=416.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=416.0, kind=None),
                                                    ),
                                                    Constant(value=416.0, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            None,
                                            Constant(value='amount_untaxed', kind=None),
                                            Constant(value='amount_tax', kind=None),
                                            Constant(value='amount_total', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='move_vals',
                                                ctx=Load(),
                                            ),
                                            Constant(value=320.0, kind=None),
                                            Constant(value=96.0, kind=None),
                                            Constant(value=416.0, kind=None),
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
                    name='test_in_invoice_line_onchange_product_2_with_fiscal_pos',
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
                            value=Constant(value=' Test mapping a price-included tax (10%) with a price-excluded tax (20%) on a price_unit of 110.0.\n        The price_unit should be 100.0 after applying the fiscal position.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='tax_price_include', ctx=Store())],
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
                                            Constant(value='type_tax_use', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='price_include', kind=None),
                                            Constant(value='include_base_amount', kind=None),
                                        ],
                                        values=[
                                            Constant(value='10% incl', kind=None),
                                            Constant(value='purchase', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=10, kind=None),
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
                            targets=[Name(id='tax_price_exclude', ctx=Store())],
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
                                            Constant(value='type_tax_use', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                        ],
                                        values=[
                                            Constant(value='15% excl', kind=None),
                                            Constant(value='purchase', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=15, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='fiscal_position', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.fiscal.position', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='tax_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='fiscal_pos_a', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=None, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='tax_src_id', kind=None),
                                                                    Constant(value='tax_dest_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='tax_price_include', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='tax_price_exclude', ctx=Load()),
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
                            targets=[Name(id='product', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='uom_id', kind=None),
                                            Constant(value='standard_price', kind=None),
                                            Constant(value='supplier_taxes_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='product', kind=None),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ref',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='uom.product_uom_unit', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=110.0, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Attribute(
                                                                value=Name(id='tax_price_include', ctx=Load()),
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
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='move_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Call(
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
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='default_move_type',
                                                value=Constant(value='in_invoice', kind=None),
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
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='partner_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='partner_a',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='invoice_date',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Date',
                                        ctx=Load(),
                                    ),
                                    attr='from_string',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='2019-01-01', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='currency_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
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
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='fiscal_position_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='fiscal_position', ctx=Load()),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='move_form', ctx=Load()),
                                                attr='invoice_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='product_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='product', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='save',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertInvoiceValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='invoice', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='tax_ids', kind=None),
                                                    Constant(value='tax_line_id', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='product', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=200.0, kind=None),
                                                    Constant(value=200.0, kind=None),
                                                    Constant(value=230.0, kind=None),
                                                    Attribute(
                                                        value=Name(id='tax_price_exclude', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=200.0, kind=None),
                                                    Constant(value=100.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='tax_ids', kind=None),
                                                    Constant(value='tax_line_id', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=False, kind=None),
                                                    Constant(value=30.0, kind=None),
                                                    Constant(value=30.0, kind=None),
                                                    Constant(value=30.0, kind=None),
                                                    List(elts=[], ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='tax_price_exclude', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=30.0, kind=None),
                                                    Constant(value=15.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='tax_ids', kind=None),
                                                    Constant(value='tax_line_id', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=False, kind=None),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=230.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=230.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=230.0, kind=None),
                                                    ),
                                                    List(elts=[], ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=230.0, kind=None),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=115.0, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='fiscal_position_id', kind=None),
                                            Constant(value='amount_untaxed', kind=None),
                                            Constant(value='amount_tax', kind=None),
                                            Constant(value='amount_total', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='currency_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='currency', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='fiscal_position', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=200.0, kind=None),
                                            Constant(value=30.0, kind=None),
                                            Constant(value=230.0, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='uom_dozen', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='uom.product_uom_dozen', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[Name(id='invoice', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='move_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='move_form', ctx=Load()),
                                                        attr='invoice_line_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='edit',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=0, kind=None)],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='line_form', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line_form', ctx=Load()),
                                                    attr='product_uom_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='uom_dozen', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertInvoiceValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='invoice', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='product_uom_id', kind=None),
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='tax_ids', kind=None),
                                                    Constant(value='tax_line_id', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='product', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='uom_dozen', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=2400.0, kind=None),
                                                    Constant(value=2400.0, kind=None),
                                                    Constant(value=2760.0, kind=None),
                                                    Attribute(
                                                        value=Name(id='tax_price_exclude', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=2400.0, kind=None),
                                                    Constant(value=1200.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='product_uom_id', kind=None),
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='tax_ids', kind=None),
                                                    Constant(value='tax_line_id', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=False, kind=None),
                                                    Constant(value=False, kind=None),
                                                    Constant(value=360.0, kind=None),
                                                    Constant(value=360.0, kind=None),
                                                    Constant(value=360.0, kind=None),
                                                    List(elts=[], ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='tax_price_exclude', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=360.0, kind=None),
                                                    Constant(value=180.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='product_uom_id', kind=None),
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='tax_ids', kind=None),
                                                    Constant(value='tax_line_id', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=False, kind=None),
                                                    Constant(value=False, kind=None),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=2760.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=2760.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=2760.0, kind=None),
                                                    ),
                                                    List(elts=[], ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=2760.0, kind=None),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=1380.0, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='fiscal_position_id', kind=None),
                                            Constant(value='amount_untaxed', kind=None),
                                            Constant(value='amount_tax', kind=None),
                                            Constant(value='amount_total', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='currency_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='currency', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='fiscal_position', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=2400.0, kind=None),
                                            Constant(value=360.0, kind=None),
                                            Constant(value=2760.0, kind=None),
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
                    name='test_in_invoice_line_onchange_product_2_with_fiscal_pos_2',
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
                            value=Constant(value=' Test mapping a price-included tax (10%) with another price-included tax (20%) on a price_unit of 110.0.\n        The price_unit should be 120.0 after applying the fiscal position.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='tax_price_include_1', ctx=Store())],
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
                                            Constant(value='type_tax_use', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='price_include', kind=None),
                                            Constant(value='include_base_amount', kind=None),
                                        ],
                                        values=[
                                            Constant(value='10% incl', kind=None),
                                            Constant(value='purchase', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=10, kind=None),
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
                            targets=[Name(id='tax_price_include_2', ctx=Store())],
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
                                            Constant(value='type_tax_use', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='price_include', kind=None),
                                            Constant(value='include_base_amount', kind=None),
                                        ],
                                        values=[
                                            Constant(value='20% incl', kind=None),
                                            Constant(value='purchase', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=20, kind=None),
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
                            targets=[Name(id='fiscal_position', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.fiscal.position', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='tax_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='fiscal_pos_a', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=None, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='tax_src_id', kind=None),
                                                                    Constant(value='tax_dest_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='tax_price_include_1', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='tax_price_include_2', ctx=Load()),
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
                            targets=[Name(id='product', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='uom_id', kind=None),
                                            Constant(value='standard_price', kind=None),
                                            Constant(value='supplier_taxes_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='product', kind=None),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ref',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='uom.product_uom_unit', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=110.0, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Attribute(
                                                                value=Name(id='tax_price_include_1', ctx=Load()),
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
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='move_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Call(
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
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='default_move_type',
                                                value=Constant(value='in_invoice', kind=None),
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
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='partner_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='partner_a',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='invoice_date',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Date',
                                        ctx=Load(),
                                    ),
                                    attr='from_string',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='2019-01-01', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='currency_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
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
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='fiscal_position_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='fiscal_position', ctx=Load()),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='move_form', ctx=Load()),
                                                attr='invoice_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='product_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='product', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='save',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertInvoiceValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='invoice', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='tax_ids', kind=None),
                                                    Constant(value='tax_line_id', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='product', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=240.0, kind=None),
                                                    Constant(value=200.0, kind=None),
                                                    Constant(value=240.0, kind=None),
                                                    Attribute(
                                                        value=Name(id='tax_price_include_2', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=200.0, kind=None),
                                                    Constant(value=100.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='tax_ids', kind=None),
                                                    Constant(value='tax_line_id', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=False, kind=None),
                                                    Constant(value=40.0, kind=None),
                                                    Constant(value=40.0, kind=None),
                                                    Constant(value=40.0, kind=None),
                                                    List(elts=[], ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='tax_price_include_2', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=40.0, kind=None),
                                                    Constant(value=20.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='tax_ids', kind=None),
                                                    Constant(value='tax_line_id', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=False, kind=None),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=240.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=240.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=240.0, kind=None),
                                                    ),
                                                    List(elts=[], ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=240.0, kind=None),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=120.0, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='fiscal_position_id', kind=None),
                                            Constant(value='amount_untaxed', kind=None),
                                            Constant(value='amount_tax', kind=None),
                                            Constant(value='amount_total', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='currency_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='currency', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='fiscal_position', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=200.0, kind=None),
                                            Constant(value=40.0, kind=None),
                                            Constant(value=240.0, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='uom_dozen', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='uom.product_uom_dozen', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[Name(id='invoice', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='move_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='move_form', ctx=Load()),
                                                        attr='invoice_line_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='edit',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=0, kind=None)],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='line_form', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line_form', ctx=Load()),
                                                    attr='product_uom_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='uom_dozen', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertInvoiceValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='invoice', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='product_uom_id', kind=None),
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='tax_ids', kind=None),
                                                    Constant(value='tax_line_id', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='product', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='uom_dozen', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=2880.0, kind=None),
                                                    Constant(value=2400.0, kind=None),
                                                    Constant(value=2880.0, kind=None),
                                                    Attribute(
                                                        value=Name(id='tax_price_include_2', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=2400.0, kind=None),
                                                    Constant(value=1200.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='product_uom_id', kind=None),
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='tax_ids', kind=None),
                                                    Constant(value='tax_line_id', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=False, kind=None),
                                                    Constant(value=False, kind=None),
                                                    Constant(value=480.0, kind=None),
                                                    Constant(value=480.0, kind=None),
                                                    Constant(value=480.0, kind=None),
                                                    List(elts=[], ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='tax_price_include_2', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=480.0, kind=None),
                                                    Constant(value=240.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='product_uom_id', kind=None),
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='tax_ids', kind=None),
                                                    Constant(value='tax_line_id', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=False, kind=None),
                                                    Constant(value=False, kind=None),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=2880.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=2880.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=2880.0, kind=None),
                                                    ),
                                                    List(elts=[], ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=2880.0, kind=None),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=1440.0, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='fiscal_position_id', kind=None),
                                            Constant(value='amount_untaxed', kind=None),
                                            Constant(value='amount_tax', kind=None),
                                            Constant(value='amount_total', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='currency_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='currency', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='fiscal_position', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=2400.0, kind=None),
                                            Constant(value=480.0, kind=None),
                                            Constant(value=2880.0, kind=None),
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
                    name='test_in_invoice_line_onchange_business_fields_1',
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
                            targets=[Name(id='move_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='move_form', ctx=Load()),
                                                attr='invoice_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='edit',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=0, kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='quantity',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=4, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='discount',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=50, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='price_unit',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=400, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertInvoiceValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='quantity', kind=None),
                                                    Constant(value='discount', kind=None),
                                                    Constant(value='price_unit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=50.0, kind=None),
                                                    Constant(value=400.0, kind=None),
                                                ],
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_line_vals_2',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tax_line_vals_1',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tax_line_vals_2',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='term_line_vals_1',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='move_vals',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='move_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='move_form', ctx=Load()),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='edit',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=2, kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='quantity',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=1, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='discount',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=100, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='price_unit',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=800, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertInvoiceValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='discount', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=100.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_line_vals_2',
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=24.0, kind=None),
                                                    Constant(value=24.0, kind=None),
                                                    Constant(value=24.0, kind=None),
                                                    Constant(value=24.0, kind=None),
                                                    Constant(value=24.0, kind=None),
                                                ],
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tax_line_vals_2',
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='term_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=208.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=208.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=208.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=208.0, kind=None),
                                                    ),
                                                    Constant(value=208.0, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            None,
                                            Constant(value='amount_untaxed', kind=None),
                                            Constant(value='amount_tax', kind=None),
                                            Constant(value='amount_total', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='move_vals',
                                                ctx=Load(),
                                            ),
                                            Constant(value=160.0, kind=None),
                                            Constant(value=48.0, kind=None),
                                            Constant(value=208.0, kind=None),
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
                    name='test_in_invoice_line_onchange_accounting_fields_1',
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
                            targets=[Name(id='move_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='move_form', ctx=Load()),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='edit',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=2, kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='debit',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=3000, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='move_form', ctx=Load()),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='edit',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=3, kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='credit',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=500, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='move_form', ctx=Load()),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='edit',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=0, kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='debit',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=800, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='move_form', ctx=Load()),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='edit',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=4, kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='debit',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=250, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertInvoiceValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=3000.0, kind=None),
                                                    Constant(value=3000.0, kind=None),
                                                    Constant(value=3450.0, kind=None),
                                                    Constant(value=3000.0, kind=None),
                                                    Constant(value=3000.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=500.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=500.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=650.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=500.0, kind=None),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=500.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=800.0, kind=None),
                                                    Constant(value=800.0, kind=None),
                                                    Constant(value=800.0, kind=None),
                                                    Constant(value=800.0, kind=None),
                                                    Constant(value=800.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=250.0, kind=None),
                                                    Constant(value=250.0, kind=None),
                                                    Constant(value=250.0, kind=None),
                                                    Constant(value=250.0, kind=None),
                                                    Constant(value=250.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='term_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=3550.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=3550.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=3550.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=3550.0, kind=None),
                                                    ),
                                                    Constant(value=3550.0, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            None,
                                            Constant(value='amount_untaxed', kind=None),
                                            Constant(value='amount_tax', kind=None),
                                            Constant(value='amount_total', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='move_vals',
                                                ctx=Load(),
                                            ),
                                            Constant(value=2500.0, kind=None),
                                            Constant(value=1050.0, kind=None),
                                            Constant(value=3550.0, kind=None),
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
                    name='test_in_invoice_line_onchange_partner_1',
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
                            targets=[Name(id='move_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='partner_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='partner_b',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='payment_reference',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='turlututu', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertInvoiceValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='partner_id', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='partner_b',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='partner_id', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='partner_b',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='partner_id', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='partner_b',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='partner_id', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='partner_b',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='name', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='date_maturity', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='term_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='turlututu', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='partner_b',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='partner_b',
                                                                ctx=Load(),
                                                            ),
                                                            attr='property_account_payable_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=789.6, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=789.6, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=789.6, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=789.6, kind=None),
                                                    ),
                                                    Constant(value=789.6, kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='fields', ctx=Load()),
                                                                attr='Date',
                                                                ctx=Load(),
                                                            ),
                                                            attr='from_string',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='2019-02-28', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='name', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='term_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='turlututu', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='partner_b',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='partner_b',
                                                                ctx=Load(),
                                                            ),
                                                            attr='property_account_payable_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=338.4, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=338.4, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=338.4, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=338.4, kind=None),
                                                    ),
                                                    Constant(value=338.4, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            None,
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='payment_reference', kind=None),
                                            Constant(value='fiscal_position_id', kind=None),
                                            Constant(value='invoice_payment_term_id', kind=None),
                                            Constant(value='amount_untaxed', kind=None),
                                            Constant(value='amount_tax', kind=None),
                                            Constant(value='amount_total', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='move_vals',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='partner_b',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='turlututu', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='fiscal_pos_a',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='pay_terms_b',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=960.0, kind=None),
                                            Constant(value=168.0, kind=None),
                                            Constant(value=1128.0, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='move_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
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
                                    value=Attribute(
                                        value=Name(id='move_form', ctx=Load()),
                                        attr='invoice_line_ids',
                                        ctx=Load(),
                                    ),
                                    attr='remove',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=0, kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='move_form', ctx=Load()),
                                        attr='invoice_line_ids',
                                        ctx=Load(),
                                    ),
                                    attr='remove',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=0, kind=None)],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='move_form', ctx=Load()),
                                                attr='invoice_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='product_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_a',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='move_form', ctx=Load()),
                                                attr='invoice_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='product_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_b',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertInvoiceValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='account_id', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='tax_ids', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_b',
                                                                ctx=Load(),
                                                            ),
                                                            attr='property_account_expense_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='partner_b',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='tax_purchase_b',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='tax_ids', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='partner_b',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=184.0, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='tax_purchase_b',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='name', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='tax_line_id', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='tax_purchase_b',
                                                            ctx=Load(),
                                                        ),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='partner_b',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='tax_purchase_b',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='name', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='date_maturity', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='term_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='turlututu', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='partner_b',
                                                                ctx=Load(),
                                                            ),
                                                            attr='property_account_payable_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='partner_b',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=772.8, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=772.8, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=772.8, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=772.8, kind=None),
                                                    ),
                                                    Constant(value=772.8, kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='fields', ctx=Load()),
                                                                attr='Date',
                                                                ctx=Load(),
                                                            ),
                                                            attr='from_string',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='2019-02-28', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='name', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='term_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='turlututu', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='partner_b',
                                                                ctx=Load(),
                                                            ),
                                                            attr='property_account_payable_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='partner_b',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=331.2, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=331.2, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=331.2, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=331.2, kind=None),
                                                    ),
                                                    Constant(value=331.2, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            None,
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='payment_reference', kind=None),
                                            Constant(value='fiscal_position_id', kind=None),
                                            Constant(value='invoice_payment_term_id', kind=None),
                                            Constant(value='amount_untaxed', kind=None),
                                            Constant(value='amount_tax', kind=None),
                                            Constant(value='amount_total', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='move_vals',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='partner_b',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='turlututu', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='fiscal_pos_a',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='pay_terms_b',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=960.0, kind=None),
                                            Constant(value=144.0, kind=None),
                                            Constant(value=1104.0, kind=None),
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
                    name='test_in_invoice_line_onchange_taxes_1',
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
                            targets=[Name(id='move_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='move_form', ctx=Load()),
                                                attr='invoice_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='edit',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=0, kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='price_unit',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=960, kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='line_form', ctx=Load()),
                                                attr='tax_ids',
                                                ctx=Load(),
                                            ),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tax_armageddon',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='child_tax_1', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tax_armageddon',
                                        ctx=Load(),
                                    ),
                                    attr='children_tax_ids',
                                    ctx=Load(),
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='child_tax_2', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tax_armageddon',
                                        ctx=Load(),
                                    ),
                                    attr='children_tax_ids',
                                    ctx=Load(),
                                ),
                                slice=Constant(value=1, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertInvoiceValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='tax_ids', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=960.0, kind=None),
                                                    Constant(value=800.0, kind=None),
                                                    Constant(value=1176.0, kind=None),
                                                    Attribute(
                                                        value=BinOp(
                                                            left=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='tax_purchase_a',
                                                                ctx=Load(),
                                                            ),
                                                            op=Add(),
                                                            right=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='tax_armageddon',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_line_vals_2',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tax_line_vals_1',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tax_line_vals_2',
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='product_uom_id', kind=None),
                                                    Constant(value='quantity', kind=None),
                                                    Constant(value='discount', kind=None),
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='tax_ids', kind=None),
                                                    Constant(value='tax_line_id', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='date_maturity', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='child_tax_1', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='company_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='default_account_tax_sale', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='partner_a',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                    Constant(value=1.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=64.0, kind=None),
                                                    Constant(value=64.0, kind=None),
                                                    Constant(value=70.4, kind=None),
                                                    Attribute(
                                                        value=Name(id='child_tax_2', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='child_tax_1', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='company_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=64.0, kind=None),
                                                    Constant(value=64.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='product_uom_id', kind=None),
                                                    Constant(value='quantity', kind=None),
                                                    Constant(value='discount', kind=None),
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='tax_ids', kind=None),
                                                    Constant(value='tax_line_id', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='date_maturity', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='child_tax_1', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='company_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='default_account_expense', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='partner_a',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                    Constant(value=1.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=96.0, kind=None),
                                                    Constant(value=96.0, kind=None),
                                                    Constant(value=105.6, kind=None),
                                                    Attribute(
                                                        value=Name(id='child_tax_2', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='child_tax_1', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='company_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=96.0, kind=None),
                                                    Constant(value=96.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='product_uom_id', kind=None),
                                                    Constant(value='quantity', kind=None),
                                                    Constant(value='discount', kind=None),
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='tax_ids', kind=None),
                                                    Constant(value='tax_line_id', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='date_maturity', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='child_tax_2', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='child_tax_2', ctx=Load()),
                                                            attr='cash_basis_transition_account_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='partner_a',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                    Constant(value=1.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=96.0, kind=None),
                                                    Constant(value=96.0, kind=None),
                                                    Constant(value=96.0, kind=None),
                                                    List(elts=[], ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='child_tax_2', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='company_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=96.0, kind=None),
                                                    Constant(value=96.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='term_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1384.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1384.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1384.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1384.0, kind=None),
                                                    ),
                                                    Constant(value=1384.0, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            None,
                                            Constant(value='amount_untaxed', kind=None),
                                            Constant(value='amount_tax', kind=None),
                                            Constant(value='amount_total', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='move_vals',
                                                ctx=Load(),
                                            ),
                                            Constant(value=960.0, kind=None),
                                            Constant(value=424.0, kind=None),
                                            Constant(value=1384.0, kind=None),
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
                    name='test_in_invoice_line_onchange_cash_rounding_1',
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
                            targets=[Name(id='move_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='invoice_cash_rounding_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='cash_rounding_a',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertInvoiceValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_line_vals_1',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_line_vals_2',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tax_line_vals_1',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tax_line_vals_2',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='term_line_vals_1',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='move_vals',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='move_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='move_form', ctx=Load()),
                                                attr='invoice_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='edit',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=0, kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='price_unit',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=799.99, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertInvoiceValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='product_uom_id', kind=None),
                                                    Constant(value='quantity', kind=None),
                                                    Constant(value='discount', kind=None),
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='tax_ids', kind=None),
                                                    Constant(value='tax_line_id', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='date_maturity', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='add_invoice_line', kind=None),
                                                    Constant(value=False, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='cash_rounding_a',
                                                                ctx=Load(),
                                                            ),
                                                            attr='loss_account_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='partner_a',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                    Constant(value=1.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=0.01, kind=None),
                                                    Constant(value=0.01, kind=None),
                                                    Constant(value=0.01, kind=None),
                                                    List(elts=[], ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='company_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=0.01, kind=None),
                                                    Constant(value=0.01, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=799.99, kind=None),
                                                    Constant(value=799.99, kind=None),
                                                    Constant(value=919.99, kind=None),
                                                    Constant(value=799.99, kind=None),
                                                    Constant(value=799.99, kind=None),
                                                ],
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_line_vals_2',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tax_line_vals_1',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tax_line_vals_2',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='term_line_vals_1',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='move_vals',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='move_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='invoice_cash_rounding_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='cash_rounding_b',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertInvoiceValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=799.99, kind=None),
                                                    Constant(value=799.99, kind=None),
                                                    Constant(value=919.99, kind=None),
                                                    Constant(value=799.99, kind=None),
                                                    Constant(value=799.99, kind=None),
                                                ],
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_line_vals_2',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tax_line_vals_1',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tax_line_vals_2',
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='product_uom_id', kind=None),
                                                    Constant(value='quantity', kind=None),
                                                    Constant(value='discount', kind=None),
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='tax_ids', kind=None),
                                                    Constant(value='tax_line_id', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='date_maturity', kind=None),
                                                ],
                                                values=[
                                                    BinOp(
                                                        left=Constant(value='%s (rounding)', kind=None),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='tax_purchase_a',
                                                                ctx=Load(),
                                                            ),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='company_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='default_account_tax_purchase', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='partner_a',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                    Constant(value=1.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=0.04, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=0.04, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=0.04, kind=None),
                                                    ),
                                                    List(elts=[], ctx=Load()),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='tax_purchase_a',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='company_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=0.04, kind=None),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=0.04, kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='term_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1127.95, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1127.95, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1127.95, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1127.95, kind=None),
                                                    ),
                                                    Constant(value=1127.95, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            None,
                                            Constant(value='amount_untaxed', kind=None),
                                            Constant(value='amount_tax', kind=None),
                                            Constant(value='amount_total', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='move_vals',
                                                ctx=Load(),
                                            ),
                                            Constant(value=959.99, kind=None),
                                            Constant(value=167.96, kind=None),
                                            Constant(value=1127.95, kind=None),
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
                    name='test_in_invoice_line_onchange_currency_1',
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
                            targets=[Name(id='move_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='currency_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='currency_data',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='currency', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertInvoiceValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=800.0, kind=None),
                                                    Constant(value=400.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=160.0, kind=None),
                                                    Constant(value=80.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=144.0, kind=None),
                                                    Constant(value=72.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=24.0, kind=None),
                                                    Constant(value=12.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='term_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1128.0, kind=None),
                                                    ),
                                                    Constant(value=564.0, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            None,
                                            Constant(value='currency_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='move_vals',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='currency_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='currency', kind=None),
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
                        ),
                        Assign(
                            targets=[Name(id='move_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='date',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Date',
                                        ctx=Load(),
                                    ),
                                    attr='from_string',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='2016-01-01', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertInvoiceValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=800.0, kind=None),
                                                    Constant(value=266.67, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=160.0, kind=None),
                                                    Constant(value=53.33, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=144.0, kind=None),
                                                    Constant(value=48.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=24.0, kind=None),
                                                    Constant(value=8.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='term_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1128.0, kind=None),
                                                    ),
                                                    Constant(value=376.0, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            None,
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='date', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='move_vals',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='currency_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='currency', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='from_string',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='2016-01-01', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='move_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='move_form', ctx=Load()),
                                                attr='invoice_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='edit',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=0, kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='quantity',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=0.1, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='price_unit',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=0.045, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertInvoiceValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='quantity', kind=None),
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=0.1, kind=None),
                                                    Constant(value=0.05, kind=None),
                                                    Constant(value=0.005, kind=None),
                                                    Constant(value=0.006, kind=None),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=0.005, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=160.0, kind=None),
                                                    Constant(value=53.33, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=24.0, kind=None),
                                                    Constant(value=24.001, kind=None),
                                                    Constant(value=24.001, kind=None),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=24.001, kind=None),
                                                    Constant(value=8.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=24.0, kind=None),
                                                    Constant(value=8.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='term_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=208.01, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=208.006, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=208.006, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=208.006, kind=None),
                                                    ),
                                                    Constant(value=69.33, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            None,
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='amount_untaxed', kind=None),
                                            Constant(value='amount_tax', kind=None),
                                            Constant(value='amount_total', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='move_vals',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='currency_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='currency', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='from_string',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='2016-01-01', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value=160.005, kind=None),
                                            Constant(value=48.001, kind=None),
                                            Constant(value=208.006, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='move_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='currency_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='company_data',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='currency', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertInvoiceValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='quantity', kind=None),
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=0.1, kind=None),
                                                    Constant(value=0.05, kind=None),
                                                    Constant(value=0.01, kind=None),
                                                    Constant(value=0.01, kind=None),
                                                    Constant(value=0.01, kind=None),
                                                    Constant(value=0.01, kind=None),
                                                ],
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_line_vals_2',
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=24.0, kind=None),
                                                    Constant(value=24.0, kind=None),
                                                    Constant(value=24.0, kind=None),
                                                    Constant(value=24.0, kind=None),
                                                    Constant(value=24.0, kind=None),
                                                ],
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tax_line_vals_2',
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='term_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=208.01, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=208.01, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=208.01, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=208.01, kind=None),
                                                    ),
                                                    Constant(value=208.01, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            None,
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='amount_untaxed', kind=None),
                                            Constant(value='amount_tax', kind=None),
                                            Constant(value='amount_total', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='move_vals',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='company_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='currency', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='from_string',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='2016-01-01', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value=160.01, kind=None),
                                            Constant(value=48.0, kind=None),
                                            Constant(value=208.01, kind=None),
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
                    name='test_in_invoice_onchange_past_invoice_1',
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
                            targets=[Name(id='copy_invoice', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='move_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
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
                                    value=Attribute(
                                        value=Name(id='move_form', ctx=Load()),
                                        attr='invoice_line_ids',
                                        ctx=Load(),
                                    ),
                                    attr='remove',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=0, kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='move_form', ctx=Load()),
                                        attr='invoice_line_ids',
                                        ctx=Load(),
                                    ),
                                    attr='remove',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=0, kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='invoice_vendor_bill_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='copy_invoice', ctx=Load()),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertInvoiceValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_line_vals_1',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_line_vals_2',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tax_line_vals_1',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tax_line_vals_2',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='term_line_vals_1',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='move_vals',
                                        ctx=Load(),
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
                    name='test_in_invoice_create_refund',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                    attr='action_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='move_reversal', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.move.reversal', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='active_model',
                                                value=Constant(value='account.move', kind=None),
                                            ),
                                            keyword(
                                                arg='active_ids',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='invoice',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='date', kind=None),
                                            Constant(value='reason', kind=None),
                                            Constant(value='refund_method', kind=None),
                                            Constant(value='journal_id', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='from_string',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='2019-02-01', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='no reason', kind=None),
                                            Constant(value='refund', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='invoice',
                                                        ctx=Load(),
                                                    ),
                                                    attr='journal_id',
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
                            targets=[Name(id='reversal', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move_reversal', ctx=Load()),
                                    attr='reverse_moves',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='reverse_move', ctx=Store())],
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
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='reversal', ctx=Load()),
                                        slice=Constant(value='res_id', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='invoice',
                                            ctx=Load(),
                                        ),
                                        attr='payment_state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='not_paid', kind=None),
                                    Constant(value="Refunding with a draft credit note should keep the invoice 'not_paid'.", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertInvoiceValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='reverse_move', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=800.0, kind=None),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=800.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=160.0, kind=None),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=160.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=144.0, kind=None),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=144.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=24.0, kind=None),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=24.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='name', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='date_maturity', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='term_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='', kind=None),
                                                    Constant(value=1128.0, kind=None),
                                                    Constant(value=1128.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Attribute(
                                                        value=Name(id='move_reversal', ctx=Load()),
                                                        attr='date',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            None,
                                            Constant(value='invoice_payment_term_id', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='state', kind=None),
                                            Constant(value='ref', kind=None),
                                            Constant(value='payment_state', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='move_vals',
                                                ctx=Load(),
                                            ),
                                            Constant(value=None, kind=None),
                                            Attribute(
                                                value=Name(id='move_reversal', ctx=Load()),
                                                attr='date',
                                                ctx=Load(),
                                            ),
                                            Constant(value='draft', kind=None),
                                            BinOp(
                                                left=Constant(value='Reversal of: %s, %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='invoice',
                                                                ctx=Load(),
                                                            ),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='move_reversal', ctx=Load()),
                                                            attr='reason',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Constant(value='not_paid', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='move_reversal', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.move.reversal', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='active_model',
                                                value=Constant(value='account.move', kind=None),
                                            ),
                                            keyword(
                                                arg='active_ids',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='invoice',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='date', kind=None),
                                            Constant(value='reason', kind=None),
                                            Constant(value='refund_method', kind=None),
                                            Constant(value='journal_id', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='from_string',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='2019-02-01', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='no reason again', kind=None),
                                            Constant(value='cancel', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='invoice',
                                                        ctx=Load(),
                                                    ),
                                                    attr='journal_id',
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
                            targets=[Name(id='reversal', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move_reversal', ctx=Load()),
                                    attr='reverse_moves',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='reverse_move', ctx=Store())],
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
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='reversal', ctx=Load()),
                                        slice=Constant(value='res_id', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='invoice',
                                            ctx=Load(),
                                        ),
                                        attr='payment_state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='reversed', kind=None),
                                    Constant(value="After cancelling it with a reverse invoice, an invoice should be in 'reversed' state.", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertInvoiceValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='reverse_move', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=800.0, kind=None),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=800.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=160.0, kind=None),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=160.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=144.0, kind=None),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=144.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=24.0, kind=None),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=24.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='name', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='date_maturity', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='term_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='', kind=None),
                                                    Constant(value=1128.0, kind=None),
                                                    Constant(value=1128.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Attribute(
                                                        value=Name(id='move_reversal', ctx=Load()),
                                                        attr='date',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            None,
                                            Constant(value='invoice_payment_term_id', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='state', kind=None),
                                            Constant(value='ref', kind=None),
                                            Constant(value='payment_state', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='move_vals',
                                                ctx=Load(),
                                            ),
                                            Constant(value=None, kind=None),
                                            Attribute(
                                                value=Name(id='move_reversal', ctx=Load()),
                                                attr='date',
                                                ctx=Load(),
                                            ),
                                            Constant(value='posted', kind=None),
                                            BinOp(
                                                left=Constant(value='Reversal of: %s, %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='invoice',
                                                                ctx=Load(),
                                                            ),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='move_reversal', ctx=Load()),
                                                            attr='reason',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Constant(value='paid', kind=None),
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
                    name='test_in_invoice_create_refund_multi_currency',
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
                            value=Constant(value=' Test the account.move.reversal takes care about the currency rates when setting\n        a custom reversal date.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='move_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='date',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='2016-01-01', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='currency_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='currency_data',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='currency', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                    attr='action_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='move_reversal', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.move.reversal', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='active_model',
                                                value=Constant(value='account.move', kind=None),
                                            ),
                                            keyword(
                                                arg='active_ids',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='invoice',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='date', kind=None),
                                            Constant(value='reason', kind=None),
                                            Constant(value='refund_method', kind=None),
                                            Constant(value='journal_id', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='from_string',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='2017-01-01', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='no reason', kind=None),
                                            Constant(value='refund', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='invoice',
                                                        ctx=Load(),
                                                    ),
                                                    attr='journal_id',
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
                            targets=[Name(id='reversal', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move_reversal', ctx=Load()),
                                    attr='reverse_moves',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='reverse_move', ctx=Store())],
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
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='reversal', ctx=Load()),
                                        slice=Constant(value='res_id', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='invoice',
                                            ctx=Load(),
                                        ),
                                        attr='payment_state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='not_paid', kind=None),
                                    Constant(value="Refunding with a draft credit note should keep the invoice 'not_paid'.", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertInvoiceValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='reverse_move', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=800.0, kind=None),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=400.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=160.0, kind=None),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=80.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=144.0, kind=None),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=72.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=24.0, kind=None),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=12.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='name', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='date_maturity', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='term_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='', kind=None),
                                                    Constant(value=1128.0, kind=None),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=564.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Attribute(
                                                        value=Name(id='move_reversal', ctx=Load()),
                                                        attr='date',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            None,
                                            Constant(value='invoice_payment_term_id', kind=None),
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='state', kind=None),
                                            Constant(value='ref', kind=None),
                                            Constant(value='payment_state', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='move_vals',
                                                ctx=Load(),
                                            ),
                                            Constant(value=None, kind=None),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='currency_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='currency', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='move_reversal', ctx=Load()),
                                                attr='date',
                                                ctx=Load(),
                                            ),
                                            Constant(value='draft', kind=None),
                                            BinOp(
                                                left=Constant(value='Reversal of: %s, %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='invoice',
                                                                ctx=Load(),
                                                            ),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='move_reversal', ctx=Load()),
                                                            attr='reason',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Constant(value='not_paid', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='move_reversal', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.move.reversal', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='active_model',
                                                value=Constant(value='account.move', kind=None),
                                            ),
                                            keyword(
                                                arg='active_ids',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='invoice',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='date', kind=None),
                                            Constant(value='reason', kind=None),
                                            Constant(value='refund_method', kind=None),
                                            Constant(value='journal_id', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='from_string',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='2017-01-01', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='no reason again', kind=None),
                                            Constant(value='cancel', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='invoice',
                                                        ctx=Load(),
                                                    ),
                                                    attr='journal_id',
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
                            targets=[Name(id='reversal', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move_reversal', ctx=Load()),
                                    attr='reverse_moves',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='reverse_move', ctx=Store())],
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
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='reversal', ctx=Load()),
                                        slice=Constant(value='res_id', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='invoice',
                                            ctx=Load(),
                                        ),
                                        attr='payment_state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='reversed', kind=None),
                                    Constant(value="After cancelling it with a reverse invoice, an invoice should be in 'reversed' state.", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertInvoiceValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='reverse_move', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=800.0, kind=None),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=400.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=160.0, kind=None),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=80.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=144.0, kind=None),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=72.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=24.0, kind=None),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=12.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='name', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='date_maturity', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='term_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='', kind=None),
                                                    Constant(value=1128.0, kind=None),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=564.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Attribute(
                                                        value=Name(id='move_reversal', ctx=Load()),
                                                        attr='date',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            None,
                                            Constant(value='invoice_payment_term_id', kind=None),
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='state', kind=None),
                                            Constant(value='ref', kind=None),
                                            Constant(value='payment_state', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='move_vals',
                                                ctx=Load(),
                                            ),
                                            Constant(value=None, kind=None),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='currency_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='currency', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='move_reversal', ctx=Load()),
                                                attr='date',
                                                ctx=Load(),
                                            ),
                                            Constant(value='posted', kind=None),
                                            BinOp(
                                                left=Constant(value='Reversal of: %s, %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='invoice',
                                                                ctx=Load(),
                                                            ),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='move_reversal', ctx=Load()),
                                                            attr='reason',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Constant(value='paid', kind=None),
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
                    name='test_in_invoice_create_1',
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
                            targets=[Name(id='move', ctx=Store())],
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
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='invoice_payment_term_id', kind=None),
                                            Constant(value='invoice_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='in_invoice', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='partner_a',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='from_string',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='2019-01-01', kind=None)],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='currency_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='currency', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='pay_terms_a',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='product_uom_id', kind=None),
                                                                    Constant(value='price_unit', kind=None),
                                                                    Constant(value='tax_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='product_id', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='product_uom_id', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='price_unit', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='Command', ctx=Load()),
                                                                                    attr='set',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='product_line_vals_1',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value='tax_ids', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='product_uom_id', kind=None),
                                                                    Constant(value='price_unit', kind=None),
                                                                    Constant(value='tax_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='product_id', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='product_uom_id', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='price_unit', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='Command', ctx=Load()),
                                                                                    attr='set',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='product_line_vals_2',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value='tax_ids', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
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
                                    attr='assertInvoiceValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='move', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=800.0, kind=None),
                                                    Constant(value=400.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=160.0, kind=None),
                                                    Constant(value=80.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=144.0, kind=None),
                                                    Constant(value=72.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=24.0, kind=None),
                                                    Constant(value=12.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='term_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1128.0, kind=None),
                                                    ),
                                                    Constant(value=564.0, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            None,
                                            Constant(value='currency_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='move_vals',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='currency_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='currency', kind=None),
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
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_in_invoice_write_1',
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
                            targets=[Name(id='move', ctx=Store())],
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
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='invoice_payment_term_id', kind=None),
                                            Constant(value='invoice_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='in_invoice', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='partner_a',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='from_string',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='2019-01-01', kind=None)],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='currency_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='currency', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='pay_terms_a',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='product_uom_id', kind=None),
                                                                    Constant(value='price_unit', kind=None),
                                                                    Constant(value='tax_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='product_id', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='product_uom_id', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='price_unit', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='Command', ctx=Load()),
                                                                                    attr='set',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='product_line_vals_1',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value='tax_ids', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
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
                                    value=Name(id='move', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='invoice_line_ids', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='product_uom_id', kind=None),
                                                                    Constant(value='price_unit', kind=None),
                                                                    Constant(value='tax_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='product_id', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='product_uom_id', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='price_unit', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='Command', ctx=Load()),
                                                                                    attr='set',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='product_line_vals_2',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value='tax_ids', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertInvoiceValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='move', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=800.0, kind=None),
                                                    Constant(value=400.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=160.0, kind=None),
                                                    Constant(value=80.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=144.0, kind=None),
                                                    Constant(value=72.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=24.0, kind=None),
                                                    Constant(value=12.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='term_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1128.0, kind=None),
                                                    ),
                                                    Constant(value=564.0, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            None,
                                            Constant(value='currency_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='move_vals',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='currency_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='currency', kind=None),
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
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_in_invoice_duplicate_supplier_reference',
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
                            value=Constant(value=" Ensure two vendor bills can't share the same vendor reference. ", kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='a supplier reference', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='default',
                                        value=Dict(
                                            keys=[Constant(value='invoice_date', kind=None)],
                                            values=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='invoice',
                                                        ctx=Load(),
                                                    ),
                                                    attr='invoice_date',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ValidationError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='invoice2', ctx=Load()),
                                            attr='ref',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='a supplier reference', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_in_invoice_switch_in_refund_1',
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
                            targets=[Name(id='move', ctx=Store())],
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
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='invoice_payment_term_id', kind=None),
                                            Constant(value='invoice_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='in_invoice', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='partner_a',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='from_string',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='2019-01-01', kind=None)],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='currency_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='currency', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='pay_terms_a',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='product_uom_id', kind=None),
                                                                    Constant(value='price_unit', kind=None),
                                                                    Constant(value='tax_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='product_id', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='product_uom_id', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='price_unit', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='Command', ctx=Load()),
                                                                                    attr='set',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='product_line_vals_1',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value='tax_ids', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='product_uom_id', kind=None),
                                                                    Constant(value='price_unit', kind=None),
                                                                    Constant(value='tax_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='product_id', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='product_uom_id', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='price_unit', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='Command', ctx=Load()),
                                                                                    attr='set',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='product_line_vals_2',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value='tax_ids', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
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
                                    value=Name(id='move', ctx=Load()),
                                    attr='action_switch_invoice_into_refund_credit_note',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='move', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[Constant(value='move_type', kind=None)],
                                                values=[Constant(value='in_refund', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertInvoiceValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='move', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=800.0, kind=None),
                                                    ),
                                                    Constant(value=400.0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=160.0, kind=None),
                                                    ),
                                                    Constant(value=80.0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=144.0, kind=None),
                                                    ),
                                                    Constant(value=72.0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=24.0, kind=None),
                                                    ),
                                                    Constant(value=12.0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='term_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=1128.0, kind=None),
                                                    Constant(value=564.0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            None,
                                            Constant(value='currency_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='move_vals',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='currency_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='currency', kind=None),
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
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_in_invoice_switch_in_refund_2',
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
                            targets=[Name(id='move', ctx=Store())],
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
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='invoice_payment_term_id', kind=None),
                                            Constant(value='invoice_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='in_invoice', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='partner_a',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='from_string',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='2019-01-01', kind=None)],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='currency_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='currency', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='pay_terms_a',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='product_uom_id', kind=None),
                                                                    Constant(value='price_unit', kind=None),
                                                                    Constant(value='quantity', kind=None),
                                                                    Constant(value='tax_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='product_id', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='product_uom_id', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='price_unit', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    UnaryOp(
                                                                        op=USub(),
                                                                        operand=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product_line_vals_1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value='quantity', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='Command', ctx=Load()),
                                                                                    attr='set',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='product_line_vals_1',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value='tax_ids', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='product_uom_id', kind=None),
                                                                    Constant(value='price_unit', kind=None),
                                                                    Constant(value='quantity', kind=None),
                                                                    Constant(value='tax_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='product_id', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='product_uom_id', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='price_unit', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    UnaryOp(
                                                                        op=USub(),
                                                                        operand=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product_line_vals_2',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value='quantity', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='Command', ctx=Load()),
                                                                                    attr='set',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='product_line_vals_2',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value='tax_ids', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
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
                                    attr='assertInvoiceValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='move', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='quantity', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=800.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=800.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=920.0, kind=None),
                                                    ),
                                                    Constant(value=400.0, kind=None),
                                                    Constant(value=0, kind=None),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1.0, kind=None),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='quantity', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=160.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=160.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=208.0, kind=None),
                                                    ),
                                                    Constant(value=80.0, kind=None),
                                                    Constant(value=0, kind=None),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1.0, kind=None),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=144.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=144.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=144.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=144.0, kind=None),
                                                    ),
                                                    Constant(value=72.0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=24.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=24.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=24.0, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=24.0, kind=None),
                                                    ),
                                                    Constant(value=12.0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='term_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=1128.0, kind=None),
                                                    Constant(value=1128.0, kind=None),
                                                    Constant(value=1128.0, kind=None),
                                                    Constant(value=1128.0, kind=None),
                                                    Constant(value=564.0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            None,
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='amount_tax', kind=None),
                                            Constant(value='amount_total', kind=None),
                                            Constant(value='amount_untaxed', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='move_vals',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='currency_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='currency', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            UnaryOp(
                                                op=USub(),
                                                operand=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='move_vals',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='amount_tax', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            UnaryOp(
                                                op=USub(),
                                                operand=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='move_vals',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='amount_total', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            UnaryOp(
                                                op=USub(),
                                                operand=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='move_vals',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='amount_untaxed', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move', ctx=Load()),
                                    attr='action_switch_invoice_into_refund_credit_note',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='move', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[Constant(value='move_type', kind=None)],
                                                values=[Constant(value='in_refund', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertInvoiceValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='move', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=800.0, kind=None),
                                                    ),
                                                    Constant(value=400.0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=160.0, kind=None),
                                                    ),
                                                    Constant(value=80.0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=144.0, kind=None),
                                                    ),
                                                    Constant(value=72.0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='debit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=24.0, kind=None),
                                                    ),
                                                    Constant(value=12.0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='term_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=1128.0, kind=None),
                                                    Constant(value=564.0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            None,
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='amount_tax', kind=None),
                                            Constant(value='amount_total', kind=None),
                                            Constant(value='amount_untaxed', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='move_vals',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='currency_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='currency', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='move_vals',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='amount_tax', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='move_vals',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='amount_total', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='move_vals',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='amount_untaxed', kind=None),
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
                    name='test_in_invoice_change_period_accrual_1',
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
                            targets=[Name(id='move', ctx=Store())],
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
                                            Constant(value='date', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='invoice_date', kind=None),
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='invoice_payment_term_id', kind=None),
                                            Constant(value='invoice_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='in_invoice', kind=None),
                                            Constant(value='2017-01-01', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='partner_a',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='from_string',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='2017-01-01', kind=None)],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='currency_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='currency', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='pay_terms_a',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=None, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='product_uom_id', kind=None),
                                                                    Constant(value='quantity', kind=None),
                                                                    Constant(value='price_unit', kind=None),
                                                                    Constant(value='tax_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='name', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='product_id', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='product_uom_id', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='quantity', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='price_unit', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='tax_ids', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=None, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='product_uom_id', kind=None),
                                                                    Constant(value='quantity', kind=None),
                                                                    Constant(value='price_unit', kind=None),
                                                                    Constant(value='tax_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='name', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='product_id', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='product_uom_id', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='quantity', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='price_unit', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_line_vals_2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='tax_ids', kind=None),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move', ctx=Load()),
                                    attr='action_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.automatic.entry.wizard', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='active_model',
                                                value=Constant(value='account.move.line', kind=None),
                                            ),
                                            keyword(
                                                arg='active_ids',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='move', ctx=Load()),
                                                        attr='invoice_line_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='action', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='percentage', kind=None),
                                            Constant(value='journal_id', kind=None),
                                            Constant(value='expense_accrual_account', kind=None),
                                            Constant(value='revenue_accrual_account', kind=None),
                                        ],
                                        values=[
                                            Constant(value='change_period', kind=None),
                                            Constant(value='2018-01-01', kind=None),
                                            Constant(value=60, kind=None),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='company_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='default_journal_misc', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='account.account', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='create',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Dict(
                                                            keys=[
                                                                Constant(value='name', kind=None),
                                                                Constant(value='code', kind=None),
                                                                Constant(value='user_type_id', kind=None),
                                                                Constant(value='reconcile', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value='Accrual Expense Account', kind=None),
                                                                Constant(value='234567', kind=None),
                                                                Attribute(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='env',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='ref',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='account.data_account_type_expenses', kind=None)],
                                                                        keywords=[],
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
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='account.account', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='create',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Dict(
                                                            keys=[
                                                                Constant(value='name', kind=None),
                                                                Constant(value='code', kind=None),
                                                                Constant(value='user_type_id', kind=None),
                                                                Constant(value='reconcile', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value='Accrual Revenue Account', kind=None),
                                                                Constant(value='765432', kind=None),
                                                                Attribute(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='env',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='ref',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='account.data_account_type_expenses', kind=None)],
                                                                        keywords=[],
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
                            targets=[Name(id='wizard_res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='wizard', ctx=Load()),
                                    attr='do_action',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertInvoiceValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='move', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=800.0, kind=None),
                                                    Constant(value=400.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=160.0, kind=None),
                                                    Constant(value=80.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=144.0, kind=None),
                                                    Constant(value=72.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tax_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=24.0, kind=None),
                                                    Constant(value=12.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='date_maturity', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='term_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1128.0, kind=None),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=564.0, kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='fields', ctx=Load()),
                                                                attr='Date',
                                                                ctx=Load(),
                                                            ),
                                                            attr='from_string',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='2017-01-01', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            None,
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='date', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='move_vals',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='currency_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='currency', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='from_string',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='2017-01-01', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='accrual_lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
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
                                                attr='browse',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Subscript(
                                                            value=Name(id='wizard_res', ctx=Load()),
                                                            slice=Constant(value='domain', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=2, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='line_ids',
                                        ctx=Load(),
                                    ),
                                    attr='sorted',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='date', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='accrual_lines', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                    Constant(value='reconciled', kind=None),
                                                ],
                                                values=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=480.0, kind=None),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=240.0, kind=None),
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='product_line_vals_1',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='account_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                    Constant(value='reconciled', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=480.0, kind=None),
                                                    Constant(value=240.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='wizard', ctx=Load()),
                                                            attr='expense_accrual_account',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=True, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                    Constant(value='reconciled', kind=None),
                                                ],
                                                values=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=96.0, kind=None),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=48.0, kind=None),
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='product_line_vals_2',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='account_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                    Constant(value='reconciled', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=96.0, kind=None),
                                                    Constant(value=48.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='wizard', ctx=Load()),
                                                            attr='expense_accrual_account',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=True, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                    Constant(value='reconciled', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=480.0, kind=None),
                                                    Constant(value=240.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='product_line_vals_1',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='account_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                    Constant(value='reconciled', kind=None),
                                                ],
                                                values=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=480.0, kind=None),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=240.0, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='wizard', ctx=Load()),
                                                            attr='expense_accrual_account',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=True, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                    Constant(value='reconciled', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=96.0, kind=None),
                                                    Constant(value=48.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='product_line_vals_2',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='account_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                    Constant(value='reconciled', kind=None),
                                                ],
                                                values=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=96.0, kind=None),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=48.0, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='wizard', ctx=Load()),
                                                            attr='expense_accrual_account',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=True, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
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
