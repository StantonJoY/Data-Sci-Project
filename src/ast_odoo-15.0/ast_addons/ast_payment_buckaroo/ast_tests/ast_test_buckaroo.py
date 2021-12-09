Module(
    body=[
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='ValidationError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='mute_logger', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='common',
            names=[alias(name='BuckarooCommon', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='controllers.main',
            names=[alias(name='BuckarooController', asname=None)],
            level=2,
        ),
        ClassDef(
            name='BuckarooTest',
            bases=[Name(id='BuckarooCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_redirect_form_values',
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
                            targets=[Name(id='return_url', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_build_url',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='BuckarooController', ctx=Load()),
                                        attr='_return_url',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='Brq_websitekey', kind=None),
                                    Constant(value='Brq_amount', kind=None),
                                    Constant(value='Brq_currency', kind=None),
                                    Constant(value='Brq_invoicenumber', kind=None),
                                    Constant(value='Brq_signature', kind=None),
                                    Constant(value='Brq_return', kind=None),
                                    Constant(value='Brq_returncancel', kind=None),
                                    Constant(value='Brq_returnerror', kind=None),
                                    Constant(value='Brq_returnreject', kind=None),
                                    Constant(value='Brq_culture', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='buckaroo',
                                            ctx=Load(),
                                        ),
                                        attr='buckaroo_website_key',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='str', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='amount',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='currency',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='reference',
                                        ctx=Load(),
                                    ),
                                    Constant(value='04c26578116990496770687a8bf225200e0f56e6', kind=None),
                                    Name(id='return_url', ctx=Load()),
                                    Name(id='return_url', ctx=Load()),
                                    Name(id='return_url', ctx=Load()),
                                    Name(id='return_url', ctx=Load()),
                                    Constant(value='en-US', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tx_sudo', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_transaction',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='flow',
                                        value=Constant(value='redirect', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='mute_logger', ctx=Load()),
                                        args=[Constant(value='odoo.addons.payment.models.payment_transaction', kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='processing_values', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tx_sudo', ctx=Load()),
                                            attr='_get_processing_values',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='form_info', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_extract_values_from_html_form',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='processing_values', ctx=Load()),
                                        slice=Constant(value='redirect_form_html', kind=None),
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
                                    Subscript(
                                        value=Name(id='form_info', ctx=Load()),
                                        slice=Constant(value='action', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='https://testcheckout.buckaroo.nl/html/', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertDictEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='expected_values', ctx=Load()),
                                    Subscript(
                                        value=Name(id='form_info', ctx=Load()),
                                        slice=Constant(value='inputs', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='Buckaroo: invalid inputs specified in the redirect form.', kind=None),
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
                    name='test_feedback_processing',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='amount',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=2240.0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='reference',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='SO004', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='buckaroo_post_data', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='BRQ_RETURNDATA', kind=None),
                                    Constant(value='BRQ_AMOUNT', kind=None),
                                    Constant(value='BRQ_CURRENCY', kind=None),
                                    Constant(value='BRQ_CUSTOMER_NAME', kind=None),
                                    Constant(value='BRQ_INVOICENUMBER', kind=None),
                                    Constant(value='brq_payment', kind=None),
                                    Constant(value='BRQ_PAYMENT_METHOD', kind=None),
                                    Constant(value='BRQ_SERVICE_PAYPAL_PAYERCOUNTRY', kind=None),
                                    Constant(value='BRQ_SERVICE_PAYPAL_PAYEREMAIL', kind=None),
                                    Constant(value='BRQ_SERVICE_PAYPAL_PAYERFIRSTNAME', kind=None),
                                    Constant(value='BRQ_SERVICE_PAYPAL_PAYERLASTNAME', kind=None),
                                    Constant(value='BRQ_SERVICE_PAYPAL_PAYERMIDDLENAME', kind=None),
                                    Constant(value='BRQ_SERVICE_PAYPAL_PAYERSTATUS', kind=None),
                                    Constant(value='Brq_signature', kind=None),
                                    Constant(value='BRQ_STATUSCODE', kind=None),
                                    Constant(value='BRQ_STATUSCODE_DETAIL', kind=None),
                                    Constant(value='BRQ_STATUSMESSAGE', kind=None),
                                    Constant(value='BRQ_TIMESTAMP', kind=None),
                                    Constant(value='BRQ_TRANSACTIONS', kind=None),
                                    Constant(value='BRQ_WEBSITEKEY', kind=None),
                                ],
                                values=[
                                    Constant(value='', kind='u'),
                                    Call(
                                        func=Name(id='str', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='amount',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='currency',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Jan de Tester', kind='u'),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='reference',
                                        ctx=Load(),
                                    ),
                                    Constant(value='573311D081B04069BD6336001611DBD4', kind='u'),
                                    Constant(value='paypal', kind='u'),
                                    Constant(value='NL', kind='u'),
                                    Constant(value='fhe@odoo.com', kind='u'),
                                    Constant(value='Jan', kind='u'),
                                    Constant(value='Tester', kind='u'),
                                    Constant(value='de', kind='u'),
                                    Constant(value='verified', kind='u'),
                                    Constant(value='e439f3af06b9752197631715628d6a198a25900f', kind='u'),
                                    Constant(value='190', kind='u'),
                                    Constant(value='S001', kind='u'),
                                    Constant(value='Transaction successfully processed', kind='u'),
                                    Constant(value='2014-05-08 12:41:21', kind='u'),
                                    Constant(value='D6106678E1D54EEB8093F5B3AC42EA7B', kind='u'),
                                    Constant(value='5xTGyGyPyl', kind='u'),
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='payment.transaction', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_handle_feedback_data',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='buckaroo', kind=None),
                                            Name(id='buckaroo_post_data', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tx', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_transaction',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='flow',
                                        value=Constant(value='redirect', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tx', ctx=Load()),
                                    attr='_handle_feedback_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='buckaroo', kind=None),
                                    Name(id='buckaroo_post_data', ctx=Load()),
                                ],
                                keywords=[],
                            ),
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
                                        value=Name(id='tx', ctx=Load()),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='done', kind=None),
                                    Constant(value='Buckaroo: validation did not put tx into done state', kind=None),
                                ],
                                keywords=[],
                            ),
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
                                        value=Name(id='tx', ctx=Load()),
                                        attr='acquirer_reference',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='buckaroo_post_data', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='BRQ_TRANSACTIONS', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='Buckaroo: validation did not update tx payid', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='reference',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='SO004-2', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tx', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_transaction',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='flow',
                                        value=Constant(value='redirect', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='buckaroo_post_data', ctx=Load()),
                                    slice=Constant(value='BRQ_INVOICENUMBER', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='reference',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='buckaroo_post_data', ctx=Load()),
                                    slice=Constant(value='Brq_signature', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='54d928810e343acf5fb0c3ee75fd747ff159ef7a', kind=None),
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='payment.transaction', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_handle_feedback_data',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='buckaroo', kind=None),
                                            Name(id='buckaroo_post_data', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='buckaroo_post_data', ctx=Load()),
                                    slice=Constant(value='BRQ_STATUSCODE', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='2', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='buckaroo_post_data', ctx=Load()),
                                    slice=Constant(value='Brq_signature', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='b8e54e26b2b5a5e697b8ed5085329ea712fd48b2', kind=None),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='mute_logger', ctx=Load()),
                                        args=[Constant(value='odoo.addons.payment_buckaroo.models.payment_transaction', kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='payment.transaction', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_handle_feedback_data',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='buckaroo', kind=None),
                                            Name(id='buckaroo_post_data', ctx=Load()),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='tx', ctx=Load()),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='error', kind=None),
                                    Constant(value='Buckaroo: unexpected status code should put tx in error state', kind=None),
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
