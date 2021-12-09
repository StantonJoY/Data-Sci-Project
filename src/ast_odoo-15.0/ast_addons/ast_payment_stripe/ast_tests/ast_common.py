Module(
    body=[
        ImportFrom(
            module='odoo.addons.payment.tests.common',
            names=[alias(name='PaymentCommon', asname=None)],
            level=0,
        ),
        ClassDef(
            name='StripeCommon',
            bases=[Name(id='PaymentCommon', ctx=Load())],
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
                                    attr='stripe',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_prepare_acquirer',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='stripe', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='update_values',
                                        value=Dict(
                                            keys=[
                                                Constant(value='stripe_secret_key', kind=None),
                                                Constant(value='stripe_publishable_key', kind=None),
                                                Constant(value='stripe_webhook_secret', kind=None),
                                                Constant(value='payment_icon_ids', kind=None),
                                            ],
                                            values=[
                                                Constant(value='sk_test_KJtHgNwt2KS3xM7QJPr4O5E8', kind=None),
                                                Constant(value='pk_test_QSPnimmb4ZhtkEy3Uhdm4S6J', kind=None),
                                                Constant(value='whsec_vG1fL6CMUouQ7cObF2VJprLVXT5jBLxB', kind=None),
                                                List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value=5, kind=None),
                                                                Constant(value=0, kind=None),
                                                                Constant(value=0, kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
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
                                    attr='acquirer',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='cls', ctx=Load()),
                                attr='stripe',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
