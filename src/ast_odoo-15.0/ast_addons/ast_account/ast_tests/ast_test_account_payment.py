Module(
    body=[
        ImportFrom(
            module='odoo.addons.account.tests.common',
            names=[alias(name='AccountTestInvoicingCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[
                alias(name='tagged', asname=None),
                alias(name='new_test_user', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='Form', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestAccountPayment',
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
                            targets=[Name(id='company_id', ctx=Store())],
                            value=Attribute(
                                value=Subscript(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='company_data',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='default_journal_bank', kind=None),
                                    ctx=Load(),
                                ),
                                attr='company_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='payment_debit_account_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='copy_account',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='company_id', ctx=Load()),
                                        attr='account_journal_payment_debit_account_id',
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
                                    value=Name(id='cls', ctx=Load()),
                                    attr='payment_credit_account_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='copy_account',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='company_id', ctx=Load()),
                                        attr='account_journal_payment_credit_account_id',
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
                                    value=Name(id='cls', ctx=Load()),
                                    attr='partner_bank_account',
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
                                        slice=Constant(value='res.partner.bank', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='acc_number', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='acc_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='BE32707171912447', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='partner_a',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='bank', kind=None),
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
                                    value=Name(id='company_id', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='account_journal_payment_debit_account_id', kind=None),
                                            Constant(value='account_journal_payment_credit_account_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='payment_debit_account_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='payment_credit_account_id',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='partner_a',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='bank_ids', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='cls', ctx=Load()),
                                                                    attr='partner_bank_account',
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
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_payment_move_sync_create_write',
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
                            targets=[Name(id='copy_receivable', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='copy_account',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_data',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='default_account_receivable', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='payment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.payment', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='amount', kind=None),
                                            Constant(value='payment_type', kind=None),
                                            Constant(value='partner_type', kind=None),
                                            Constant(value='destination_account_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value=50.0, kind=None),
                                            Constant(value='inbound', kind=None),
                                            Constant(value='customer', kind=None),
                                            Attribute(
                                                value=Name(id='copy_receivable', ctx=Load()),
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
                            targets=[Name(id='expected_payment_values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='amount', kind=None),
                                    Constant(value='payment_type', kind=None),
                                    Constant(value='partner_type', kind=None),
                                    Constant(value='payment_reference', kind=None),
                                    Constant(value='is_reconciled', kind=None),
                                    Constant(value='currency_id', kind=None),
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='destination_account_id', kind=None),
                                    Constant(value='payment_method_line_id', kind=None),
                                    Constant(value='partner_bank_id', kind=None),
                                ],
                                values=[
                                    Constant(value=50.0, kind=None),
                                    Constant(value='inbound', kind=None),
                                    Constant(value='customer', kind=None),
                                    Constant(value=False, kind=None),
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
                                    Constant(value=False, kind=None),
                                    Attribute(
                                        value=Name(id='copy_receivable', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='inbound_payment_method_line',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_move_values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='currency_id', kind=None),
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='partner_bank_id', kind=None),
                                ],
                                values=[
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
                                    Constant(value=False, kind=None),
                                    Constant(value=False, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_liquidity_line', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='debit', kind=None),
                                    Constant(value='credit', kind=None),
                                    Constant(value='amount_currency', kind=None),
                                    Constant(value='currency_id', kind=None),
                                    Constant(value='account_id', kind=None),
                                ],
                                values=[
                                    Constant(value=50.0, kind=None),
                                    Constant(value=0.0, kind=None),
                                    Constant(value=50.0, kind=None),
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
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='payment_debit_account_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_counterpart_line', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='debit', kind=None),
                                    Constant(value='credit', kind=None),
                                    Constant(value='amount_currency', kind=None),
                                    Constant(value='currency_id', kind=None),
                                    Constant(value='account_id', kind=None),
                                ],
                                values=[
                                    Constant(value=0.0, kind=None),
                                    Constant(value=50.0, kind=None),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=50.0, kind=None),
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
                                    Attribute(
                                        value=Name(id='copy_receivable', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Name(id='payment', ctx=Load()),
                                    List(
                                        elts=[Name(id='expected_payment_values', ctx=Load())],
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
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='payment', ctx=Load()),
                                        attr='move_id',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Name(id='expected_move_values', ctx=Load())],
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
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='payment', ctx=Load()),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='sorted',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='balance', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Name(id='expected_counterpart_line', ctx=Load()),
                                            Name(id='expected_liquidity_line', ctx=Load()),
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
                                    value=Name(id='payment', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='partner_type', kind=None),
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='partner_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='supplier', kind=None),
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
                                                    attr='partner_a',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='payment', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='partner_type', kind=None),
                                                    Constant(value='destination_account_id', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='partner_bank_id', kind=None),
                                                ],
                                                values=[
                                                    Name(id='expected_payment_values', ctx=Load()),
                                                    Constant(value='supplier', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='partner_a',
                                                                ctx=Load(),
                                                            ),
                                                            attr='property_account_payable_id',
                                                            ctx=Load(),
                                                        ),
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
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='partner_a',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='partner_bank_account',
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
                                    Attribute(
                                        value=Name(id='payment', ctx=Load()),
                                        attr='move_id',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='partner_bank_id', kind=None),
                                                ],
                                                values=[
                                                    Name(id='expected_move_values', ctx=Load()),
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
                                                            attr='partner_a',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='partner_bank_account',
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
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='payment', ctx=Load()),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='sorted',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='balance', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                ],
                                                values=[
                                                    Name(id='expected_counterpart_line', ctx=Load()),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=25.0, kind=None),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=50.0, kind=None),
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
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='partner_a',
                                                                ctx=Load(),
                                                            ),
                                                            attr='property_account_payable_id',
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
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                ],
                                                values=[
                                                    Name(id='expected_liquidity_line', ctx=Load()),
                                                    Constant(value=25.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=50.0, kind=None),
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
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='liquidity_lines', ctx=Store()),
                                        Name(id='counterpart_lines', ctx=Store()),
                                        Name(id='writeoff_lines', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='payment', ctx=Load()),
                                    attr='_seek_for_lines',
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
                                    value=Attribute(
                                        value=Name(id='payment', ctx=Load()),
                                        attr='move_id',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='partner_bank_id', kind=None),
                                            Constant(value='line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=1, kind=None),
                                                            Attribute(
                                                                value=Name(id='counterpart_lines', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='debit', kind=None),
                                                                    Constant(value='credit', kind=None),
                                                                    Constant(value='amount_currency', kind=None),
                                                                    Constant(value='currency_id', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='partner_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value=0.0, kind=None),
                                                                    Constant(value=75.0, kind=None),
                                                                    UnaryOp(
                                                                        op=USub(),
                                                                        operand=Constant(value=75.0, kind=None),
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
                                                                    Attribute(
                                                                        value=Name(id='copy_receivable', ctx=Load()),
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
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=1, kind=None),
                                                            Attribute(
                                                                value=Name(id='liquidity_lines', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='debit', kind=None),
                                                                    Constant(value='credit', kind=None),
                                                                    Constant(value='amount_currency', kind=None),
                                                                    Constant(value='currency_id', kind=None),
                                                                    Constant(value='partner_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value=100.0, kind=None),
                                                                    Constant(value=0.0, kind=None),
                                                                    Constant(value=100.0, kind=None),
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
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='debit', kind=None),
                                                                    Constant(value='credit', kind=None),
                                                                    Constant(value='amount_currency', kind=None),
                                                                    Constant(value='currency_id', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='partner_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value=0.0, kind=None),
                                                                    Constant(value=25.0, kind=None),
                                                                    UnaryOp(
                                                                        op=USub(),
                                                                        operand=Constant(value=25.0, kind=None),
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
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='payment', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='amount', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                ],
                                                values=[
                                                    Name(id='expected_payment_values', ctx=Load()),
                                                    Constant(value=100.0, kind=None),
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
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='payment', ctx=Load()),
                                        attr='move_id',
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
                                                    Name(id='expected_move_values', ctx=Load()),
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
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='payment', ctx=Load()),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='sorted',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='balance', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                ],
                                                values=[
                                                    Name(id='expected_counterpart_line', ctx=Load()),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=75.0, kind=None),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=75.0, kind=None),
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
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=25.0, kind=None),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=25.0, kind=None),
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
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                ],
                                                values=[
                                                    Name(id='expected_liquidity_line', ctx=Load()),
                                                    Constant(value=100.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=100.0, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='payment_debit_account_id',
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
                FunctionDef(
                    name='test_payment_move_sync_onchange',
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
                            targets=[Name(id='pay_form', ctx=Store())],
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
                                                slice=Constant(value='account.payment', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='default_journal_id',
                                                value=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='company_data',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='default_journal_bank', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
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
                                    value=Name(id='pay_form', ctx=Load()),
                                    attr='amount',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=50.0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='pay_form', ctx=Load()),
                                    attr='payment_type',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='inbound', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='pay_form', ctx=Load()),
                                    attr='partner_type',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='customer', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='pay_form', ctx=Load()),
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
                            targets=[Name(id='payment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='pay_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_payment_values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='amount', kind=None),
                                    Constant(value='payment_type', kind=None),
                                    Constant(value='partner_type', kind=None),
                                    Constant(value='payment_reference', kind=None),
                                    Constant(value='is_reconciled', kind=None),
                                    Constant(value='currency_id', kind=None),
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='destination_account_id', kind=None),
                                    Constant(value='payment_method_line_id', kind=None),
                                ],
                                values=[
                                    Constant(value=50.0, kind=None),
                                    Constant(value='inbound', kind=None),
                                    Constant(value='customer', kind=None),
                                    Constant(value=False, kind=None),
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
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='partner_a',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='partner_a',
                                                ctx=Load(),
                                            ),
                                            attr='property_account_receivable_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='inbound_payment_method_line',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_move_values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='currency_id', kind=None),
                                    Constant(value='partner_id', kind=None),
                                ],
                                values=[
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
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='partner_a',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_liquidity_line', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='debit', kind=None),
                                    Constant(value='credit', kind=None),
                                    Constant(value='amount_currency', kind=None),
                                    Constant(value='currency_id', kind=None),
                                    Constant(value='account_id', kind=None),
                                ],
                                values=[
                                    Constant(value=50.0, kind=None),
                                    Constant(value=0.0, kind=None),
                                    Constant(value=50.0, kind=None),
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
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='payment_debit_account_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_counterpart_line', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='debit', kind=None),
                                    Constant(value='credit', kind=None),
                                    Constant(value='amount_currency', kind=None),
                                    Constant(value='currency_id', kind=None),
                                    Constant(value='account_id', kind=None),
                                ],
                                values=[
                                    Constant(value=0.0, kind=None),
                                    Constant(value=50.0, kind=None),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=50.0, kind=None),
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
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='default_account_receivable', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Name(id='payment', ctx=Load()),
                                    List(
                                        elts=[Name(id='expected_payment_values', ctx=Load())],
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
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='payment', ctx=Load()),
                                        attr='move_id',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Name(id='expected_move_values', ctx=Load())],
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
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='payment', ctx=Load()),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='sorted',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='balance', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Name(id='expected_counterpart_line', ctx=Load()),
                                            Name(id='expected_liquidity_line', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='pay_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[Name(id='payment', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='pay_form', ctx=Load()),
                                    attr='partner_type',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='supplier', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='pay_form', ctx=Load()),
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
                                    value=Name(id='pay_form', ctx=Load()),
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
                            targets=[Name(id='payment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='pay_form', ctx=Load()),
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
                                    Name(id='payment', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='partner_type', kind=None),
                                                    Constant(value='destination_account_id', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                ],
                                                values=[
                                                    Name(id='expected_payment_values', ctx=Load()),
                                                    Constant(value='supplier', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='partner_a',
                                                                ctx=Load(),
                                                            ),
                                                            attr='property_account_payable_id',
                                                            ctx=Load(),
                                                        ),
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
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='partner_a',
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
                                    Attribute(
                                        value=Name(id='payment', ctx=Load()),
                                        attr='move_id',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                ],
                                                values=[
                                                    Name(id='expected_move_values', ctx=Load()),
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
                                                            attr='partner_a',
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
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='payment', ctx=Load()),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='sorted',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='balance', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                ],
                                                values=[
                                                    Name(id='expected_counterpart_line', ctx=Load()),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=25.0, kind=None),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=50.0, kind=None),
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
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='partner_a',
                                                                ctx=Load(),
                                                            ),
                                                            attr='property_account_payable_id',
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
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                ],
                                                values=[
                                                    Name(id='expected_liquidity_line', ctx=Load()),
                                                    Constant(value=25.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=50.0, kind=None),
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
                                        value=Name(id='payment', ctx=Load()),
                                        attr='move_id',
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
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='amount_currency',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=100.0, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
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
                                        args=[Constant(value=1, kind=None)],
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
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='amount_currency',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=75.0, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='account_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_data',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='default_account_receivable', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
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
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='amount_currency',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=25.0, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='account_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_data',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='default_account_revenue', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
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
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='payment', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='amount', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                ],
                                                values=[
                                                    Name(id='expected_payment_values', ctx=Load()),
                                                    Constant(value=100.0, kind=None),
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
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='payment', ctx=Load()),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='sorted',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='balance', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                ],
                                                values=[
                                                    Name(id='expected_counterpart_line', ctx=Load()),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=75.0, kind=None),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=75.0, kind=None),
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
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=25.0, kind=None),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=25.0, kind=None),
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
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                ],
                                                values=[
                                                    Name(id='expected_liquidity_line', ctx=Load()),
                                                    Constant(value=100.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=100.0, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='payment_debit_account_id',
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
                FunctionDef(
                    name='test_inbound_payment_sync_writeoff_debit_sign',
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
                            targets=[Name(id='payment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.payment', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='amount', kind=None),
                                            Constant(value='payment_type', kind=None),
                                            Constant(value='partner_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value=100.0, kind=None),
                                            Constant(value='inbound', kind=None),
                                            Constant(value='customer', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='liquidity_lines', ctx=Store()),
                                        Name(id='counterpart_lines', ctx=Store()),
                                        Name(id='dummy', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='payment', ctx=Load()),
                                    attr='_seek_for_lines',
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
                                    value=Attribute(
                                        value=Name(id='payment', ctx=Load()),
                                        attr='move_id',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='line_ids', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=1, kind=None),
                                                            Attribute(
                                                                value=Name(id='liquidity_lines', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Dict(
                                                                keys=[Constant(value='debit', kind=None)],
                                                                values=[Constant(value=100.0, kind=None)],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=1, kind=None),
                                                            Attribute(
                                                                value=Name(id='counterpart_lines', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Dict(
                                                                keys=[Constant(value='credit', kind=None)],
                                                                values=[Constant(value=125.0, kind=None)],
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
                                                                    Constant(value='debit', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value=25.0, kind=None),
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
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='payment', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='payment_type', kind=None),
                                                    Constant(value='partner_type', kind=None),
                                                    Constant(value='amount', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='inbound', kind=None),
                                                    Constant(value='customer', kind=None),
                                                    Constant(value=100.0, kind=None),
                                                ],
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
                                    value=Name(id='payment', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='partner_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='destination_account_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='supplier', kind=None),
                                            Constant(value=100.1, kind=None),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='company_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='default_account_payable', kind=None),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='payment', ctx=Load()),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='sorted',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='balance', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=125.1, kind=None),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='company_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='default_account_payable', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=25.0, kind=None),
                                                    Constant(value=0.0, kind=None),
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
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=100.1, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='payment_debit_account_id',
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
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_inbound_payment_sync_writeoff_credit_sign',
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
                            targets=[Name(id='payment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.payment', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='amount', kind=None),
                                            Constant(value='payment_type', kind=None),
                                            Constant(value='partner_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value=100.0, kind=None),
                                            Constant(value='inbound', kind=None),
                                            Constant(value='customer', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='liquidity_lines', ctx=Store()),
                                        Name(id='counterpart_lines', ctx=Store()),
                                        Name(id='dummy', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='payment', ctx=Load()),
                                    attr='_seek_for_lines',
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
                                    value=Attribute(
                                        value=Name(id='payment', ctx=Load()),
                                        attr='move_id',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='line_ids', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=1, kind=None),
                                                            Attribute(
                                                                value=Name(id='liquidity_lines', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Dict(
                                                                keys=[Constant(value='debit', kind=None)],
                                                                values=[Constant(value=100.0, kind=None)],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=1, kind=None),
                                                            Attribute(
                                                                value=Name(id='counterpart_lines', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Dict(
                                                                keys=[Constant(value='credit', kind=None)],
                                                                values=[Constant(value=75.0, kind=None)],
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
                                                                    Constant(value='credit', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value=25.0, kind=None),
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
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='payment', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='payment_type', kind=None),
                                                    Constant(value='partner_type', kind=None),
                                                    Constant(value='amount', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='inbound', kind=None),
                                                    Constant(value='customer', kind=None),
                                                    Constant(value=100.0, kind=None),
                                                ],
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
                                    value=Name(id='payment', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='partner_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='destination_account_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='supplier', kind=None),
                                            Constant(value=100.1, kind=None),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='company_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='default_account_payable', kind=None),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='payment', ctx=Load()),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='sorted',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='balance', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=75.1, kind=None),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='company_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='default_account_payable', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=25.0, kind=None),
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
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=100.1, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='payment_debit_account_id',
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
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_outbound_payment_sync_writeoff_debit_sign',
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
                            targets=[Name(id='payment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.payment', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='amount', kind=None),
                                            Constant(value='payment_type', kind=None),
                                            Constant(value='partner_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value=100.0, kind=None),
                                            Constant(value='outbound', kind=None),
                                            Constant(value='supplier', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='liquidity_lines', ctx=Store()),
                                        Name(id='counterpart_lines', ctx=Store()),
                                        Name(id='dummy', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='payment', ctx=Load()),
                                    attr='_seek_for_lines',
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
                                    value=Attribute(
                                        value=Name(id='payment', ctx=Load()),
                                        attr='move_id',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='line_ids', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=1, kind=None),
                                                            Attribute(
                                                                value=Name(id='liquidity_lines', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Dict(
                                                                keys=[Constant(value='credit', kind=None)],
                                                                values=[Constant(value=100.0, kind=None)],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=1, kind=None),
                                                            Attribute(
                                                                value=Name(id='counterpart_lines', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Dict(
                                                                keys=[Constant(value='debit', kind=None)],
                                                                values=[Constant(value=75.0, kind=None)],
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
                                                                    Constant(value='debit', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value=25.0, kind=None),
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
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='payment', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='payment_type', kind=None),
                                                    Constant(value='partner_type', kind=None),
                                                    Constant(value='amount', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='outbound', kind=None),
                                                    Constant(value='supplier', kind=None),
                                                    Constant(value=100.0, kind=None),
                                                ],
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
                                    value=Name(id='payment', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='partner_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='destination_account_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='customer', kind=None),
                                            Constant(value=100.1, kind=None),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='company_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='default_account_receivable', kind=None),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='payment', ctx=Load()),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='sorted',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='balance', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=100.1, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='payment_credit_account_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=25.0, kind=None),
                                                    Constant(value=0.0, kind=None),
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
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=75.1, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='company_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='default_account_receivable', kind=None),
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
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_outbound_payment_sync_writeoff_credit_sign',
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
                            targets=[Name(id='payment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.payment', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='amount', kind=None),
                                            Constant(value='payment_type', kind=None),
                                            Constant(value='partner_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value=100.0, kind=None),
                                            Constant(value='outbound', kind=None),
                                            Constant(value='supplier', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='liquidity_lines', ctx=Store()),
                                        Name(id='counterpart_lines', ctx=Store()),
                                        Name(id='dummy', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='payment', ctx=Load()),
                                    attr='_seek_for_lines',
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
                                    value=Attribute(
                                        value=Name(id='payment', ctx=Load()),
                                        attr='move_id',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='line_ids', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=1, kind=None),
                                                            Attribute(
                                                                value=Name(id='liquidity_lines', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Dict(
                                                                keys=[Constant(value='credit', kind=None)],
                                                                values=[Constant(value=100.0, kind=None)],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=1, kind=None),
                                                            Attribute(
                                                                value=Name(id='counterpart_lines', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Dict(
                                                                keys=[Constant(value='debit', kind=None)],
                                                                values=[Constant(value=125.0, kind=None)],
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
                                                                    Constant(value='credit', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value=25.0, kind=None),
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
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='payment', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='payment_type', kind=None),
                                                    Constant(value='partner_type', kind=None),
                                                    Constant(value='amount', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='outbound', kind=None),
                                                    Constant(value='supplier', kind=None),
                                                    Constant(value=100.0, kind=None),
                                                ],
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
                                    value=Name(id='payment', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='partner_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='destination_account_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='customer', kind=None),
                                            Constant(value=100.1, kind=None),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='company_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='default_account_receivable', kind=None),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='payment', ctx=Load()),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='sorted',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='balance', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=100.1, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='payment_credit_account_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=25.0, kind=None),
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
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='account_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=125.1, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='company_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='default_account_receivable', kind=None),
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
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_internal_transfer',
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
                            targets=[Name(id='copy_receivable', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='copy_account',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_data',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='default_account_receivable', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='payment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.payment', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='amount', kind=None),
                                            Constant(value='is_internal_transfer', kind=None),
                                            Constant(value='destination_journal_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value=50.0, kind=None),
                                            Constant(value=True, kind=None),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='company_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='default_journal_cash', kind=None),
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
                            targets=[Name(id='expected_payment_values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='amount', kind=None),
                                    Constant(value='payment_type', kind=None),
                                    Constant(value='currency_id', kind=None),
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='destination_account_id', kind=None),
                                ],
                                values=[
                                    Constant(value=50.0, kind=None),
                                    Constant(value='inbound', kind=None),
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
                                    Attribute(
                                        value=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='company_data',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='company', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='company_data',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='company', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='transfer_account_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_move_values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='currency_id', kind=None),
                                    Constant(value='partner_id', kind=None),
                                ],
                                values=[
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
                                    Attribute(
                                        value=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='company_data',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='company', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_liquidity_line', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='debit', kind=None),
                                    Constant(value='credit', kind=None),
                                    Constant(value='amount_currency', kind=None),
                                    Constant(value='currency_id', kind=None),
                                    Constant(value='account_id', kind=None),
                                ],
                                values=[
                                    Constant(value=50.0, kind=None),
                                    Constant(value=0.0, kind=None),
                                    Constant(value=50.0, kind=None),
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
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='payment_debit_account_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_counterpart_line', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='debit', kind=None),
                                    Constant(value='credit', kind=None),
                                    Constant(value='amount_currency', kind=None),
                                    Constant(value='currency_id', kind=None),
                                    Constant(value='account_id', kind=None),
                                ],
                                values=[
                                    Constant(value=0.0, kind=None),
                                    Constant(value=50.0, kind=None),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=50.0, kind=None),
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
                                    Attribute(
                                        value=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='company_data',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='company', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='transfer_account_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Name(id='payment', ctx=Load()),
                                    List(
                                        elts=[Name(id='expected_payment_values', ctx=Load())],
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
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='payment', ctx=Load()),
                                        attr='move_id',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Name(id='expected_move_values', ctx=Load())],
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
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='payment', ctx=Load()),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='sorted',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='balance', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Name(id='expected_counterpart_line', ctx=Load()),
                                            Name(id='expected_liquidity_line', ctx=Load()),
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
                                    value=Name(id='payment', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='partner_type', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='destination_account_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='customer', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='partner_a',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='copy_receivable', ctx=Load()),
                                                attr='id',
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
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='payment', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='partner_type', kind=None),
                                                    Constant(value='destination_account_id', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='is_internal_transfer', kind=None),
                                                ],
                                                values=[
                                                    Name(id='expected_payment_values', ctx=Load()),
                                                    Constant(value='customer', kind=None),
                                                    Attribute(
                                                        value=Name(id='copy_receivable', ctx=Load()),
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
                                                ],
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
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='payment', ctx=Load()),
                                        attr='move_id',
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
                                                    Name(id='expected_move_values', ctx=Load()),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='partner_a',
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
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='payment', ctx=Load()),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='sorted',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='balance', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    None,
                                                    Constant(value='account_id', kind=None),
                                                ],
                                                values=[
                                                    Name(id='expected_counterpart_line', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='copy_receivable', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Name(id='expected_liquidity_line', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='liquidity_lines', ctx=Store()),
                                        Name(id='counterpart_lines', ctx=Store()),
                                        Name(id='writeoff_lines', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='payment', ctx=Load()),
                                    attr='_seek_for_lines',
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
                                    value=Attribute(
                                        value=Name(id='payment', ctx=Load()),
                                        attr='move_id',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='line_ids', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=1, kind=None),
                                                            Attribute(
                                                                value=Name(id='counterpart_lines', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='partner_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Subscript(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='company_data',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                slice=Constant(value='company', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='transfer_account_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Subscript(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='company_data',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                slice=Constant(value='company', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='partner_id',
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
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=1, kind=None),
                                                            Attribute(
                                                                value=Name(id='liquidity_lines', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Dict(
                                                                keys=[Constant(value='partner_id', kind=None)],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Subscript(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='company_data',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                slice=Constant(value='company', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='partner_id',
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
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='payment', ctx=Load()),
                                    List(
                                        elts=[Name(id='expected_payment_values', ctx=Load())],
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
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='payment', ctx=Load()),
                                        attr='move_id',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Name(id='expected_move_values', ctx=Load())],
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
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='payment', ctx=Load()),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='sorted',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='balance', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Name(id='expected_counterpart_line', ctx=Load()),
                                            Name(id='expected_liquidity_line', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='payment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.payment', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='amount', kind=None),
                                            Constant(value='is_internal_transfer', kind=None),
                                            Constant(value='payment_type', kind=None),
                                            Constant(value='destination_journal_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value=50.0, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value='inbound', kind=None),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='company_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='default_journal_cash', kind=None),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='payment', ctx=Load()),
                                    attr='action_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='paired_payment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.payment', kind=None),
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
                                                    Constant(value='payment_type', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='outbound', kind=None),
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
                            targets=[Name(id='expected_payment_values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='amount', kind=None),
                                    Constant(value='payment_type', kind=None),
                                    Constant(value='currency_id', kind=None),
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='destination_account_id', kind=None),
                                ],
                                values=[
                                    Constant(value=50.0, kind=None),
                                    Constant(value='outbound', kind=None),
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
                                    Attribute(
                                        value=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='company_data',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='company', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='company_data',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='company', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='transfer_account_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_move_values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='currency_id', kind=None),
                                    Constant(value='partner_id', kind=None),
                                ],
                                values=[
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
                                    Attribute(
                                        value=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='company_data',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='company', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_liquidity_line', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='debit', kind=None),
                                    Constant(value='credit', kind=None),
                                    Constant(value='amount_currency', kind=None),
                                    Constant(value='currency_id', kind=None),
                                    Constant(value='account_id', kind=None),
                                ],
                                values=[
                                    Constant(value=0.0, kind=None),
                                    Constant(value=50.0, kind=None),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=50.0, kind=None),
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
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='company_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='default_journal_cash', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='account_journal_payment_credit_account_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_counterpart_line', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='debit', kind=None),
                                    Constant(value='credit', kind=None),
                                    Constant(value='amount_currency', kind=None),
                                    Constant(value='currency_id', kind=None),
                                    Constant(value='account_id', kind=None),
                                ],
                                values=[
                                    Constant(value=50.0, kind=None),
                                    Constant(value=0.0, kind=None),
                                    Constant(value=50.0, kind=None),
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
                                    Attribute(
                                        value=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='company_data',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='company', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='transfer_account_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Name(id='paired_payment', ctx=Load()),
                                    List(
                                        elts=[Name(id='expected_payment_values', ctx=Load())],
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
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='paired_payment', ctx=Load()),
                                        attr='move_id',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Name(id='expected_move_values', ctx=Load())],
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
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='paired_payment', ctx=Load()),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='sorted',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='balance', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Name(id='expected_liquidity_line', ctx=Load()),
                                            Name(id='expected_counterpart_line', ctx=Load()),
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
                FunctionDef(
                    name='test_compute_currency_id',
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
                            value=Constant(value=' When creating a new account.payment without specifying a currency, the default currency should be the one\n        set on the journal.\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_data',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='default_journal_bank', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='currency_id', kind=None)],
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
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='payment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.payment', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='amount', kind=None),
                                            Constant(value='payment_type', kind=None),
                                            Constant(value='partner_type', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='journal_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value=50.0, kind=None),
                                            Constant(value='inbound', kind=None),
                                            Constant(value='customer', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='partner_a',
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
                                                    slice=Constant(value='default_journal_bank', kind=None),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='payment', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[Constant(value='currency_id', kind=None)],
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
                                                ],
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
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='payment', ctx=Load()),
                                        attr='move_id',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[Constant(value='currency_id', kind=None)],
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
                                                ],
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
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='payment', ctx=Load()),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='sorted',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='balance', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=25.0, kind=None),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=50.0, kind=None),
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
                                            Dict(
                                                keys=[
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=25.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=50.0, kind=None),
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
                    name='test_reconciliation_payment_states',
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
                            targets=[Name(id='payment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.payment', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='amount', kind=None),
                                            Constant(value='payment_type', kind=None),
                                            Constant(value='partner_type', kind=None),
                                            Constant(value='destination_account_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value=50.0, kind=None),
                                            Constant(value='inbound', kind=None),
                                            Constant(value='customer', kind=None),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='company_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='default_account_receivable', kind=None),
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
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='liquidity_lines', ctx=Store()),
                                        Name(id='counterpart_lines', ctx=Store()),
                                        Name(id='writeoff_lines', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='payment', ctx=Load()),
                                    attr='_seek_for_lines',
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
                                    Name(id='payment', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='is_reconciled', kind=None),
                                                    Constant(value='is_matched', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=False, kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='invoice', ctx=Store())],
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
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='price_unit', kind=None),
                                                                    Constant(value='quantity', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='50 to pay', kind=None),
                                                                    Constant(value=50.0, kind=None),
                                                                    Constant(value=1, kind=None),
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
                                    value=Name(id='payment', ctx=Load()),
                                    attr='action_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='invoice', ctx=Load()),
                                    attr='action_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=BinOp(
                                        left=Name(id='counterpart_lines', ctx=Load()),
                                        op=Add(),
                                        right=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='invoice', ctx=Load()),
                                                    attr='line_ids',
                                                    ctx=Load(),
                                                ),
                                                attr='filtered',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Lambda(
                                                    args=arguments(
                                                        posonlyargs=[],
                                                        args=[arg(arg='line', annotation=None, type_comment=None)],
                                                        vararg=None,
                                                        kwonlyargs=[],
                                                        kw_defaults=[],
                                                        kwarg=None,
                                                        defaults=[],
                                                    ),
                                                    body=Compare(
                                                        left=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='account_internal_type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='receivable', kind=None)],
                                                    ),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    attr='reconcile',
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
                                    Name(id='payment', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='is_reconciled', kind=None),
                                                    Constant(value='is_matched', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=True, kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='statement', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.bank.statement', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='journal_id', kind=None),
                                            Constant(value='line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_statement', kind=None),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='company_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='default_journal_bank', kind=None),
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
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='payment_ref', kind=None),
                                                                    Constant(value='partner_id', kind=None),
                                                                    Constant(value='amount', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='50 to pay', kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='partner_a',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
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
                                    value=Name(id='statement', ctx=Load()),
                                    attr='button_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='statement_line', ctx=Store())],
                            value=Attribute(
                                value=Name(id='statement', ctx=Load()),
                                attr='line_ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='statement_line', ctx=Load()),
                                    attr='reconcile',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[Constant(value='id', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='liquidity_lines', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='payment', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='is_reconciled', kind=None),
                                                    Constant(value='is_matched', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=True, kind=None),
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
                FunctionDef(
                    name='test_payment_name',
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
                            targets=[Name(id='AccountPayment', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='account.payment', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='AccountPayment', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='payment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='AccountPayment', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='journal_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='company_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='default_journal_bank', kind=None),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertRegex',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='payment', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='BNK1/\\d{4}/\\d{2}/0001', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='AccountPayment', ctx=Load()),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='default_move_journal_types',
                                                        value=Tuple(
                                                            elts=[
                                                                Constant(value='bank', kind=None),
                                                                Constant(value='cash', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='payment_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='payment_form', ctx=Load()),
                                                    attr='_values',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='name', kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value='/', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='payment_form', ctx=Load()),
                                            attr='journal_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_data',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='default_journal_cash', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRegex',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='payment_form', ctx=Load()),
                                                    attr='_values',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='name', kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value='CSH1/\\d{4}/\\d{2}/0001', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='payment_form', ctx=Load()),
                                            attr='journal_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_data',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='default_journal_bank', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='payment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='payment_form', ctx=Load()),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='payment', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='/', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='payment', ctx=Load()),
                                    attr='action_post',
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
                                    attr='assertRegex',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='payment', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='BNK1/\\d{4}/\\d{2}/0002', kind=None),
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
                    name='test_payment_without_default_company_account',
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
                            value=Constant(value=' The purpose of this test is to check the specific behavior when duplicating an inbound payment, then change\n        the copy to an outbound payment when we set the outstanding accounts (payments and receipts) on a journal but\n        not on the company level.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='company', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='company_data',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='company', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bank_journal', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
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
                                    value=Attribute(
                                        value=Name(id='bank_journal', ctx=Load()),
                                        attr='outbound_payment_method_line_ids',
                                        ctx=Load(),
                                    ),
                                    attr='payment_account_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='company', ctx=Load()),
                                attr='account_journal_payment_credit_account_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='bank_journal', ctx=Load()),
                                        attr='inbound_payment_method_line_ids',
                                        ctx=Load(),
                                    ),
                                    attr='payment_account_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='company', ctx=Load()),
                                attr='account_journal_payment_debit_account_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='company', ctx=Load()),
                                    attr='account_journal_payment_debit_account_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='company', ctx=Load()),
                                    attr='account_journal_payment_credit_account_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='payment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.payment', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='amount', kind=None),
                                            Constant(value='payment_type', kind=None),
                                            Constant(value='partner_type', kind=None),
                                            Constant(value='journal_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value=5.0, kind=None),
                                            Constant(value='inbound', kind=None),
                                            Constant(value='customer', kind=None),
                                            Attribute(
                                                value=Name(id='bank_journal', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='payment', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='amount', kind=None),
                                                    Constant(value='payment_type', kind=None),
                                                    Constant(value='partner_type', kind=None),
                                                    Constant(value='payment_reference', kind=None),
                                                    Constant(value='is_reconciled', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='payment_method_line_id', kind=None),
                                                    Constant(value='partner_bank_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=5.0, kind=None),
                                                    Constant(value='inbound', kind=None),
                                                    Constant(value='customer', kind=None),
                                                    Constant(value=False, kind=None),
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
                                                    Constant(value=False, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='inbound_payment_method_line',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='payment', ctx=Load()),
                                    attr='payment_type',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='outbound', kind=None),
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
                                    Name(id='payment', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='amount', kind=None),
                                                    Constant(value='payment_type', kind=None),
                                                    Constant(value='partner_type', kind=None),
                                                    Constant(value='payment_reference', kind=None),
                                                    Constant(value='is_reconciled', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='payment_method_line_id', kind=None),
                                                    Constant(value='partner_bank_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=5.0, kind=None),
                                                    Constant(value='outbound', kind=None),
                                                    Constant(value='customer', kind=None),
                                                    Constant(value=False, kind=None),
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
                                                    Constant(value=False, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='outbound_payment_method_line',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
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
