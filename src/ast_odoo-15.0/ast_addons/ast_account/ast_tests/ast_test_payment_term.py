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
        ImportFrom(
            module='odoo',
            names=[alias(name='fields', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='Form', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestAccountInvoiceRounding',
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
                                    attr='pay_term_today',
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
                                        slice=Constant(value='account.payment.term', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Today', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='value', kind=None),
                                                                    Constant(value='days', kind=None),
                                                                    Constant(value='option', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='balance', kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value='day_after_invoice_date', kind=None),
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
                                    attr='pay_term_min_31days_15th',
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
                                        slice=Constant(value='account.payment.term', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='the 15th of the month, min 31 days from now', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='value', kind=None),
                                                                    Constant(value='days', kind=None),
                                                                    Constant(value='day_of_the_month', kind=None),
                                                                    Constant(value='option', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='balance', kind=None),
                                                                    Constant(value=31, kind=None),
                                                                    Constant(value=15, kind=None),
                                                                    Constant(value='day_after_invoice_date', kind=None),
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
                                    attr='pay_term_45_end_month',
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
                                        slice=Constant(value='account.payment.term', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='45 Days from End of Month', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='value', kind=None),
                                                                    Constant(value='days', kind=None),
                                                                    Constant(value='option', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='balance', kind=None),
                                                                    Constant(value=45, kind=None),
                                                                    Constant(value='after_invoice_month', kind=None),
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
                                    attr='pay_term_last_day_of_month',
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
                                        slice=Constant(value='account.payment.term', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Last Day of month', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='value', kind=None),
                                                                    Constant(value='days', kind=None),
                                                                    Constant(value='option', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='balance', kind=None),
                                                                    Constant(value=31, kind=None),
                                                                    Constant(value='day_current_month', kind=None),
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
                                    attr='pay_term_first_day_next_month',
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
                                        slice=Constant(value='account.payment.term', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='First day next month', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='value', kind=None),
                                                                    Constant(value='days', kind=None),
                                                                    Constant(value='option', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='balance', kind=None),
                                                                    Constant(value=1, kind=None),
                                                                    Constant(value='day_following_month', kind=None),
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
                                args=[Constant(value='out_refund', kind=None)],
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
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='assertPaymentTerm',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='pay_term', annotation=None, type_comment=None),
                            arg(arg='invoice_date', annotation=None, type_comment=None),
                            arg(arg='dates', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
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
                                            attr='invoice_payment_term_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='pay_term', ctx=Load()),
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
                                    value=Name(id='invoice_date', ctx=Load()),
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
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='invoice',
                                                            ctx=Load(),
                                                        ),
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
                                                            args=[arg(arg='l', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=Compare(
                                                            left=Attribute(
                                                                value=Name(id='l', ctx=Load()),
                                                                attr='account_id',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[
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
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='date_maturity', kind=None)],
                                        keywords=[],
                                    ),
                                    ListComp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='fields', ctx=Load()),
                                                    attr='Date',
                                                    ctx=Load(),
                                                ),
                                                attr='from_string',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='date', ctx=Load())],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='date', ctx=Store()),
                                                iter=Name(id='dates', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
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
                    name='test_payment_term',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertPaymentTerm',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='pay_term_today',
                                        ctx=Load(),
                                    ),
                                    Constant(value='2019-01-01', kind=None),
                                    List(
                                        elts=[Constant(value='2019-01-01', kind=None)],
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
                                    attr='assertPaymentTerm',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='pay_term_today',
                                        ctx=Load(),
                                    ),
                                    Constant(value='2019-01-15', kind=None),
                                    List(
                                        elts=[Constant(value='2019-01-15', kind=None)],
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
                                    attr='assertPaymentTerm',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='pay_term_today',
                                        ctx=Load(),
                                    ),
                                    Constant(value='2019-01-31', kind=None),
                                    List(
                                        elts=[Constant(value='2019-01-31', kind=None)],
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
                                    attr='assertPaymentTerm',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='pay_term_45_end_month',
                                        ctx=Load(),
                                    ),
                                    Constant(value='2019-01-01', kind=None),
                                    List(
                                        elts=[Constant(value='2019-03-17', kind=None)],
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
                                    attr='assertPaymentTerm',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='pay_term_45_end_month',
                                        ctx=Load(),
                                    ),
                                    Constant(value='2019-01-15', kind=None),
                                    List(
                                        elts=[Constant(value='2019-03-17', kind=None)],
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
                                    attr='assertPaymentTerm',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='pay_term_45_end_month',
                                        ctx=Load(),
                                    ),
                                    Constant(value='2019-01-31', kind=None),
                                    List(
                                        elts=[Constant(value='2019-03-17', kind=None)],
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
                                    attr='assertPaymentTerm',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='pay_term_min_31days_15th',
                                        ctx=Load(),
                                    ),
                                    Constant(value='2019-01-01', kind=None),
                                    List(
                                        elts=[Constant(value='2019-02-15', kind=None)],
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
                                    attr='assertPaymentTerm',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='pay_term_min_31days_15th',
                                        ctx=Load(),
                                    ),
                                    Constant(value='2019-01-15', kind=None),
                                    List(
                                        elts=[Constant(value='2019-02-15', kind=None)],
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
                                    attr='assertPaymentTerm',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='pay_term_min_31days_15th',
                                        ctx=Load(),
                                    ),
                                    Constant(value='2019-01-31', kind=None),
                                    List(
                                        elts=[Constant(value='2019-03-15', kind=None)],
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
                                    attr='assertPaymentTerm',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='pay_term_last_day_of_month',
                                        ctx=Load(),
                                    ),
                                    Constant(value='2019-01-01', kind=None),
                                    List(
                                        elts=[Constant(value='2019-01-31', kind=None)],
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
                                    attr='assertPaymentTerm',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='pay_term_last_day_of_month',
                                        ctx=Load(),
                                    ),
                                    Constant(value='2019-01-15', kind=None),
                                    List(
                                        elts=[Constant(value='2019-01-31', kind=None)],
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
                                    attr='assertPaymentTerm',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='pay_term_last_day_of_month',
                                        ctx=Load(),
                                    ),
                                    Constant(value='2019-01-31', kind=None),
                                    List(
                                        elts=[Constant(value='2019-01-31', kind=None)],
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
                                    attr='assertPaymentTerm',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='pay_term_first_day_next_month',
                                        ctx=Load(),
                                    ),
                                    Constant(value='2019-01-01', kind=None),
                                    List(
                                        elts=[Constant(value='2019-02-01', kind=None)],
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
                                    attr='assertPaymentTerm',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='pay_term_first_day_next_month',
                                        ctx=Load(),
                                    ),
                                    Constant(value='2019-01-15', kind=None),
                                    List(
                                        elts=[Constant(value='2019-02-01', kind=None)],
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
                                    attr='assertPaymentTerm',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='pay_term_first_day_next_month',
                                        ctx=Load(),
                                    ),
                                    Constant(value='2019-01-31', kind=None),
                                    List(
                                        elts=[Constant(value='2019-02-01', kind=None)],
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
