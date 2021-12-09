Module(
    body=[
        ImportFrom(
            module='odoo.addons.payment.tests.common',
            names=[alias(name='PaymentCommon', asname=None)],
            level=0,
        ),
        ClassDef(
            name='PayumoneyCommon',
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
                                    attr='payumoney',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_prepare_acquirer',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='payumoney', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='update_values',
                                        value=Dict(
                                            keys=[
                                                Constant(value='payumoney_merchant_key', kind=None),
                                                Constant(value='payumoney_merchant_salt', kind=None),
                                            ],
                                            values=[
                                                Constant(value='dummy', kind=None),
                                                Constant(value='dummy', kind=None),
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
                                attr='payumoney',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='currency',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_prepare_currency',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='INR', kind=None)],
                                keywords=[],
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
