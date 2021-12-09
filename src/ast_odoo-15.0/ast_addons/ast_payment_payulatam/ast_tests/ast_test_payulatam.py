Module(
    body=[
        ImportFrom(
            module='freezegun',
            names=[alias(name='freeze_time', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='ValidationError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.fields',
            names=[alias(name='Command', asname=None)],
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
            names=[alias(name='PayULatamCommon', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='controllers.main',
            names=[alias(name='PayuLatamController', asname=None)],
            level=2,
        ),
        ImportFrom(
            module='models.payment_acquirer',
            names=[alias(name='SUPPORTED_CURRENCIES', asname=None)],
            level=2,
        ),
        ClassDef(
            name='PayULatamTest',
            bases=[Name(id='PayULatamCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_compatibility_with_supported_currencies',
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
                            value=Constant(value=' Test that the PayULatam acquirer is compatible with all supported currencies. ', kind=None),
                        ),
                        For(
                            target=Name(id='supported_currency_code', ctx=Store()),
                            iter=Name(id='SUPPORTED_CURRENCIES', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='supported_currency', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_prepare_currency',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='supported_currency_code', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='compatible_acquirers', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='payment.acquirer', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_get_compatible_acquirers',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='company',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='partner',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='currency_id',
                                                value=Attribute(
                                                    value=Name(id='supported_currency', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='payulatam',
                                                ctx=Load(),
                                            ),
                                            Name(id='compatible_acquirers', ctx=Load()),
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
                    name='test_incompatibility_with_unsupported_currency',
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
                            value=Constant(value=' Test that the PayULatam acquirer is not compatible with an unsupported currency. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='compatible_acquirers', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='payment.acquirer', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get_compatible_acquirers',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='partner',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='currency_id',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='currency_euro',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertNotIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='payulatam',
                                        ctx=Load(),
                                    ),
                                    Name(id='compatible_acquirers', ctx=Load()),
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
                    name='test_reference_is_singularized',
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
                            value=Constant(value=' Test singularization of reference prefixes. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='reference', ctx=Store())],
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
                                    attr='_compute_reference',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='payulatam',
                                            ctx=Load(),
                                        ),
                                        attr='provider',
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
                                    Name(id='reference', ctx=Load()),
                                    Constant(value='tx-20111102120021', kind=None),
                                    Constant(value='transaction reference was not correctly singularized', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='freeze_time', ctx=Load()),
                            args=[Constant(value='2011-11-02 12:00:21', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_reference_is_computed_based_on_document_name',
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
                            value=Constant(value=' Test computation of reference prefixes based on the provided invoice. ', kind=None),
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
                                args=[Dict(keys=[], values=[])],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='reference', ctx=Store())],
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
                                    attr='_compute_reference',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='payulatam',
                                            ctx=Load(),
                                        ),
                                        attr='provider',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='invoice_ids',
                                        value=List(
                                            elts=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='Command', ctx=Load()),
                                                        attr='set',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        List(
                                                            elts=[
                                                                Attribute(
                                                                    value=Name(id='invoice', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
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
                                    Name(id='reference', ctx=Load()),
                                    Constant(value='MISC/2011/11/0001-20111102120021', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='freeze_time', ctx=Load()),
                            args=[Constant(value='2011-11-02 12:00:21', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
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
                        Expr(
                            value=Constant(value=' Test the values of the redirect form inputs. ', kind=None),
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
                                            value=Name(id='tx', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='expected_values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='merchantId', kind=None),
                                    Constant(value='accountId', kind=None),
                                    Constant(value='description', kind=None),
                                    Constant(value='referenceCode', kind=None),
                                    Constant(value='amount', kind=None),
                                    Constant(value='currency', kind=None),
                                    Constant(value='tax', kind=None),
                                    Constant(value='taxReturnBase', kind=None),
                                    Constant(value='buyerEmail', kind=None),
                                    Constant(value='buyerFullName', kind=None),
                                    Constant(value='responseUrl', kind=None),
                                    Constant(value='test', kind=None),
                                ],
                                values=[
                                    Constant(value='dummy', kind=None),
                                    Constant(value='dummy', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='reference',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='reference',
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
                                    Call(
                                        func=Name(id='str', ctx=Load()),
                                        args=[Constant(value=0, kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='str', ctx=Load()),
                                        args=[Constant(value=0, kind=None)],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='partner',
                                            ctx=Load(),
                                        ),
                                        attr='email',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='partner',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_build_url',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='PayuLatamController', ctx=Load()),
                                                attr='_return_url',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='str', ctx=Load()),
                                        args=[Constant(value=1, kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='expected_values', ctx=Load()),
                                    slice=Constant(value='signature', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='payulatam',
                                        ctx=Load(),
                                    ),
                                    attr='_payulatam_generate_sign',
                                    ctx=Load(),
                                ),
                                args=[Name(id='expected_values', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='incoming',
                                        value=Constant(value=False, kind=None),
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
                                    Subscript(
                                        value=Name(id='form_info', ctx=Load()),
                                        slice=Constant(value='action', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='https://sandbox.checkout.payulatam.com/ppp-web-gateway-payu/', kind=None),
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
                                    Subscript(
                                        value=Name(id='form_info', ctx=Load()),
                                        slice=Constant(value='inputs', kind=None),
                                        ctx=Load(),
                                    ),
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
                            targets=[Name(id='payulatam_post_data', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='installmentsNumber', kind=None),
                                    Constant(value='lapPaymentMethod', kind=None),
                                    Constant(value='description', kind=None),
                                    Constant(value='currency', kind=None),
                                    Constant(value='extra2', kind=None),
                                    Constant(value='lng', kind=None),
                                    Constant(value='transactionState', kind=None),
                                    Constant(value='polPaymentMethod', kind=None),
                                    Constant(value='pseCycle', kind=None),
                                    Constant(value='pseBank', kind=None),
                                    Constant(value='referenceCode', kind=None),
                                    Constant(value='reference_pol', kind=None),
                                    Constant(value='signature', kind=None),
                                    Constant(value='pseReference3', kind=None),
                                    Constant(value='buyerEmail', kind=None),
                                    Constant(value='lapResponseCode', kind=None),
                                    Constant(value='pseReference2', kind=None),
                                    Constant(value='cus', kind=None),
                                    Constant(value='orderLanguage', kind=None),
                                    Constant(value='TX_VALUE', kind=None),
                                    Constant(value='risk', kind=None),
                                    Constant(value='trazabilityCode', kind=None),
                                    Constant(value='extra3', kind=None),
                                    Constant(value='pseReference1', kind=None),
                                    Constant(value='polTransactionState', kind=None),
                                    Constant(value='polResponseCode', kind=None),
                                    Constant(value='merchant_name', kind=None),
                                    Constant(value='merchant_url', kind=None),
                                    Constant(value='extra1', kind=None),
                                    Constant(value='message', kind=None),
                                    Constant(value='lapPaymentMethodType', kind=None),
                                    Constant(value='polPaymentMethodType', kind=None),
                                    Constant(value='telephone', kind=None),
                                    Constant(value='merchantId', kind=None),
                                    Constant(value='transactionId', kind=None),
                                    Constant(value='authorizationCode', kind=None),
                                    Constant(value='lapTransactionState', kind=None),
                                    Constant(value='TX_TAX', kind=None),
                                    Constant(value='merchant_address', kind=None),
                                ],
                                values=[
                                    Constant(value='1', kind=None),
                                    Constant(value='VISA', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='reference',
                                        ctx=Load(),
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
                                    Constant(value='', kind=None),
                                    Constant(value='es', kind=None),
                                    Constant(value='7', kind=None),
                                    Constant(value='211', kind=None),
                                    Constant(value='', kind=None),
                                    Constant(value='', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='reference',
                                        ctx=Load(),
                                    ),
                                    Constant(value='844164756', kind=None),
                                    Constant(value='f3ea3a7414a56d8153c425ab7e2f69d7', kind=None),
                                    Constant(value='', kind=None),
                                    Constant(value='admin@yourcompany.example.com', kind=None),
                                    Constant(value='PENDING_TRANSACTION_CONFIRMATION', kind=None),
                                    Constant(value='', kind=None),
                                    Constant(value='', kind=None),
                                    Constant(value='es', kind=None),
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
                                    Constant(value='', kind=None),
                                    Constant(value='', kind=None),
                                    Constant(value='', kind=None),
                                    Constant(value='', kind=None),
                                    Constant(value='14', kind=None),
                                    Constant(value='25', kind=None),
                                    Constant(value='Test PayU Test comercio', kind=None),
                                    Constant(value='http://pruebaslapv.xtrweb.com', kind=None),
                                    Constant(value='/shop/payment/validate', kind=None),
                                    Constant(value='PENDING', kind=None),
                                    Constant(value='CARD', kind=None),
                                    Constant(value='7', kind=None),
                                    Constant(value='7512354', kind=None),
                                    Constant(value='dummy', kind=None),
                                    Constant(value='b232989a-4aa8-42d1-bace-153236eee791', kind=None),
                                    Constant(value='', kind=None),
                                    Constant(value='PENDING', kind=None),
                                    Constant(value='.00', kind=None),
                                    Constant(value='Av 123 Calle 12', kind=None),
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
                                            Constant(value='payulatam', kind=None),
                                            Name(id='payulatam_post_data', ctx=Load()),
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
                                    Constant(value='payulatam', kind=None),
                                    Name(id='payulatam_post_data', ctx=Load()),
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
                                    Constant(value='pending', kind=None),
                                    Constant(value='Payulatam: wrong state after receiving a valid pending notification', kind=None),
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
                                        attr='state_message',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='payulatam_post_data', ctx=Load()),
                                        slice=Constant(value='message', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='Payulatam: wrong state message after receiving a valid pending notification', kind=None),
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
                                    Constant(value='b232989a-4aa8-42d1-bace-153236eee791', kind=None),
                                    Constant(value='Payulatam: wrong txn_id after receiving a valid pending notification', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tx', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='state', kind=None),
                                            Constant(value='acquirer_reference', kind=None),
                                        ],
                                        values=[
                                            Constant(value='draft', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='payulatam_post_data', ctx=Load()),
                                    slice=Constant(value='lapTransactionState', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='APPROVED', kind=None),
                            type_comment=None,
                        ),
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
                                    Constant(value='payulatam', kind=None),
                                    Name(id='payulatam_post_data', ctx=Load()),
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
                                    Constant(value='Payulatam: wrong state after receiving a valid pending notification', kind=None),
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
                                    Constant(value='b232989a-4aa8-42d1-bace-153236eee791', kind=None),
                                    Constant(value='Payulatam: wrong txn_id after receiving a valid pending notification', kind=None),
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
