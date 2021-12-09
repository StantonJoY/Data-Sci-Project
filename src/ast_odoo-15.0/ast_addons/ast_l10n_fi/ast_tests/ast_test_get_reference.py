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
            name='InvoiceGetReferenceTest',
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
                        defaults=[Constant(value='l10n_fi.fi_chart_template', kind=None)],
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
                                args=[Constant(value='out_invoice', kind=None)],
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
                    name='test_get_reference_finnish_invoice',
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
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='invoice',
                                            ctx=Load(),
                                        ),
                                        attr='payment_reference',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
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
                                    attr='invoice_reference_model',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='fi', kind=None),
                            type_comment=None,
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='invoice',
                                            ctx=Load(),
                                        ),
                                        attr='payment_reference',
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
                    name='test_get_reference_finnish_partner',
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
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='invoice',
                                            ctx=Load(),
                                        ),
                                        attr='payment_reference',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
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
                                    attr='invoice_reference_type',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='partner', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
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
                                    attr='invoice_reference_model',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='fi', kind=None),
                            type_comment=None,
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='invoice',
                                            ctx=Load(),
                                        ),
                                        attr='payment_reference',
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
                    name='test_get_reference_finnish_rf_invoice',
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
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='invoice',
                                            ctx=Load(),
                                        ),
                                        attr='payment_reference',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
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
                                    attr='invoice_reference_model',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='fi_rf', kind=None),
                            type_comment=None,
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='invoice',
                                            ctx=Load(),
                                        ),
                                        attr='payment_reference',
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
                    name='test_get_reference_finnish_rf_partner',
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
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='invoice',
                                            ctx=Load(),
                                        ),
                                        attr='payment_reference',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
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
                                    attr='invoice_reference_type',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='partner', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
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
                                    attr='invoice_reference_model',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='fi_rf', kind=None),
                            type_comment=None,
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='invoice',
                                            ctx=Load(),
                                        ),
                                        attr='payment_reference',
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
                        Constant(value='post_install_l10n', kind=None),
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
