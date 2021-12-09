Module(
    body=[
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
        ClassDef(
            name='TestAccountMoveInRefundOnchanges',
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
                                args=[Constant(value='in_refund', kind=None)],
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
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=800.0, kind=None),
                                    ),
                                    Constant(value=0.0, kind=None),
                                    Constant(value=800.0, kind=None),
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
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=160.0, kind=None),
                                    ),
                                    Constant(value=0.0, kind=None),
                                    Constant(value=160.0, kind=None),
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
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=144.0, kind=None),
                                    ),
                                    Constant(value=0.0, kind=None),
                                    Constant(value=144.0, kind=None),
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
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=24.0, kind=None),
                                    ),
                                    Constant(value=0.0, kind=None),
                                    Constant(value=24.0, kind=None),
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
                                    Constant(value=1128.0, kind=None),
                                    Constant(value=1128.0, kind=None),
                                    Constant(value=0.0, kind=None),
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
                                            Name(id='TestAccountMoveInRefundOnchanges', ctx=Load()),
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
                    name='test_in_refund_line_onchange_product_1',
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
                                                    Constant(value='credit', kind=None),
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
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=160.0, kind=None),
                                                    ),
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
                                                    Constant(value='credit', kind=None),
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
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=48.0, kind=None),
                                                    ),
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
                                                        attr='tax_line_vals_2',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=48.0, kind=None),
                                                    Constant(value=48.0, kind=None),
                                                    Constant(value=48.0, kind=None),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=48.0, kind=None),
                                                    ),
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
                                                    Constant(value=416.0, kind=None),
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
                    name='test_in_refund_line_onchange_business_fields_1',
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
                                                    Constant(value='credit', kind=None),
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
                                                    Constant(value='credit', kind=None),
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
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=24.0, kind=None),
                                                    ),
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
                                                    Constant(value='debit', kind=None),
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
                                                    Constant(value=208.0, kind=None),
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
                    name='test_in_refund_line_onchange_accounting_fields_1',
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
                                            attr='credit',
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
                                            attr='debit',
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
                                            attr='credit',
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
                                            attr='credit',
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
                                                    Constant(value='credit', kind=None),
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
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=3000.0, kind=None),
                                                    ),
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
                                                    Constant(value=500.0, kind=None),
                                                    Constant(value=500.0, kind=None),
                                                    Constant(value=0.0, kind=None),
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
                                                        attr='tax_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=800.0, kind=None),
                                                    Constant(value=800.0, kind=None),
                                                    Constant(value=800.0, kind=None),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=800.0, kind=None),
                                                    ),
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
                                                    Constant(value='credit', kind=None),
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
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=250.0, kind=None),
                                                    ),
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
                                                    Constant(value='debit', kind=None),
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
                                                    Constant(value=3550.0, kind=None),
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
                    name='test_in_refund_line_onchange_partner_1',
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
                                                    Constant(value='debit', kind=None),
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
                                                    Constant(value=338.4, kind=None),
                                                    Constant(value=338.4, kind=None),
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
                                                    Constant(value='debit', kind=None),
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
                                                    Constant(value=789.6, kind=None),
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
                                                    Constant(value='debit', kind=None),
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
                                                    Constant(value=331.2, kind=None),
                                                    Constant(value=331.2, kind=None),
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
                                                    Constant(value='debit', kind=None),
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
                                                    Constant(value=772.8, kind=None),
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
                    name='test_in_refund_line_onchange_taxes_1',
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
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=96.0, kind=None),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=96.0, kind=None),
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
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=64.0, kind=None),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=64.0, kind=None),
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
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=96.0, kind=None),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=96.0, kind=None),
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
                                                    Constant(value=1384.0, kind=None),
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
                    name='test_in_refund_line_onchange_cash_rounding_1',
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
                                                            attr='profit_account_id',
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
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=0.01, kind=None),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=0.01, kind=None),
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
                                                        attr='product_line_vals_1',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=799.99, kind=None),
                                                    Constant(value=799.99, kind=None),
                                                    Constant(value=919.99, kind=None),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=799.99, kind=None),
                                                    ),
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
                                                    Constant(value='credit', kind=None),
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
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=799.99, kind=None),
                                                    ),
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
                                                    Constant(value=0.04, kind=None),
                                                    Constant(value=0.04, kind=None),
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
                                                    Constant(value=1127.95, kind=None),
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
                    name='test_in_refund_line_onchange_currency_1',
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
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=800.0, kind=None),
                                                    ),
                                                    Constant(value=400.0, kind=None),
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
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=800.0, kind=None),
                                                    ),
                                                    Constant(value=266.67, kind=None),
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
                                                    Constant(value=53.33, kind=None),
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
                                                    Constant(value=48.0, kind=None),
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
                                                    Constant(value='credit', kind=None),
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
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=0.005, kind=None),
                                                    ),
                                                    Constant(value=0.0, kind=None),
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
                                                    Constant(value='credit', kind=None),
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
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=24.001, kind=None),
                                                    ),
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
                                                    Constant(value='debit', kind=None),
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
                                                    Constant(value=208.006, kind=None),
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
                                                    Constant(value='credit', kind=None),
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
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=0.01, kind=None),
                                                    ),
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
                                                    Constant(value='credit', kind=None),
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
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=24.0, kind=None),
                                                    ),
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
                                                    Constant(value='debit', kind=None),
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
                                                    Constant(value=208.01, kind=None),
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
                    name='test_in_refund_onchange_past_invoice_1',
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
                    name='test_in_refund_create_1',
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
                                            Constant(value='in_refund', kind=None),
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
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=800.0, kind=None),
                                                    ),
                                                    Constant(value=400.0, kind=None),
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
                    name='test_in_refund_write_1',
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
                                            Constant(value='in_refund', kind=None),
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
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=800.0, kind=None),
                                                    ),
                                                    Constant(value=400.0, kind=None),
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
