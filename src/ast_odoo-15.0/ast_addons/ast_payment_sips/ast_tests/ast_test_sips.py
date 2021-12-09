Module(
    body=[
        Import(
            names=[alias(name='json', asname=None)],
        ),
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
            names=[alias(name='SipsCommon', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='controllers.main',
            names=[alias(name='SipsController', asname=None)],
            level=2,
        ),
        ImportFrom(
            module='models.payment_acquirer',
            names=[alias(name='SUPPORTED_CURRENCIES', asname=None)],
            level=2,
        ),
        ClassDef(
            name='SipsTest',
            bases=[Name(id='SipsCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_compatible_acquirers',
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
                            target=Name(id='curr', ctx=Store()),
                            iter=Name(id='SUPPORTED_CURRENCIES', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='currency', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_prepare_currency',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='curr', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='acquirers', ctx=Store())],
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
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='partner_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='partner',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='company_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='company',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='currency_id',
                                                value=Attribute(
                                                    value=Name(id='currency', ctx=Load()),
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
                                                attr='sips',
                                                ctx=Load(),
                                            ),
                                            Name(id='acquirers', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='unsupported_currency', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_currency',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='VEF', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='acquirers', ctx=Store())],
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
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='partner_id',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='partner',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='company_id',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='currency_id',
                                        value=Attribute(
                                            value=Name(id='unsupported_currency', ctx=Load()),
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
                                        attr='sips',
                                        ctx=Load(),
                                    ),
                                    Name(id='acquirers', ctx=Load()),
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
                    name='test_reference',
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
                                    keyword(
                                        arg='reference',
                                        value=Constant(value='', kind=None),
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
                                    Attribute(
                                        value=Name(id='tx', ctx=Load()),
                                        attr='reference',
                                        ctx=Load(),
                                    ),
                                    Constant(value='tx20111102120021', kind=None),
                                    Constant(value="Payulatam: transaction reference wasn't correctly singularized.", kind=None),
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
                            targets=[Name(id='form_inputs', ctx=Store())],
                            value=Subscript(
                                value=Name(id='form_info', ctx=Load()),
                                slice=Constant(value='inputs', kind=None),
                                ctx=Load(),
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
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sips',
                                            ctx=Load(),
                                        ),
                                        attr='sips_test_url',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='form_inputs', ctx=Load()),
                                        slice=Constant(value='InterfaceVersion', kind=None),
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sips',
                                            ctx=Load(),
                                        ),
                                        attr='sips_version',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                        value=Name(id='SipsController', ctx=Load()),
                                        attr='_return_url',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='notify_url', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_build_url',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='SipsController', ctx=Load()),
                                        attr='_notify_url',
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
                                        value=Name(id='form_inputs', ctx=Load()),
                                        slice=Constant(value='Data', kind=None),
                                        ctx=Load(),
                                    ),
                                    JoinedStr(
                                        values=[
                                            Constant(value='amount=111111|currencyCode=978|merchantId=dummy_mid|normalReturnUrl=', kind=None),
                                            FormattedValue(
                                                value=Name(id='return_url', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='|automaticResponseUrl=', kind=None),
                                            FormattedValue(
                                                value=Name(id='notify_url', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='|transactionReference=', kind=None),
                                            FormattedValue(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='reference',
                                                    ctx=Load(),
                                                ),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='|statementReference=', kind=None),
                                            FormattedValue(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='reference',
                                                    ctx=Load(),
                                                ),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='|keyVersion=', kind=None),
                                            FormattedValue(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='sips',
                                                        ctx=Load(),
                                                    ),
                                                    attr='sips_key_version',
                                                    ctx=Load(),
                                                ),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='|returnContext=', kind=None),
                                            FormattedValue(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='json', ctx=Load()),
                                                        attr='dumps',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Call(
                                                            func=Name(id='dict', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='reference',
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='reference',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                conversion=-1,
                                                format_spec=None,
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='form_inputs', ctx=Load()),
                                        slice=Constant(value='Seal', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='4d7cc67c0168e8ce11c25fbe1937231c644861e320702ab544022b032b9eb4a2', kind=None),
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
                            targets=[Name(id='sips_post_data', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='Data', kind=None),
                                    Constant(value='Encode', kind=None),
                                    Constant(value='InterfaceVersion', kind=None),
                                    Constant(value='Seal', kind=None),
                                    Constant(value='locale', kind=None),
                                ],
                                values=[
                                    Constant(value='captureDay=0|captureMode=AUTHOR_CAPTURE|currencyCode=840|merchantId=002001000000001|orderChannel=INTERNET|responseCode=00|transactionDateTime=2020-04-08T06:15:59+02:00|transactionReference=SO100x1|keyVersion=1|acquirerResponseCode=00|amount=31400|authorisationId=0020000006791167|paymentMeanBrand=IDEAL|paymentMeanType=CREDIT_TRANSFER|customerIpAddress=127.0.0.1|returnContext={"return_url": "/payment/process", "reference": "SO100x1"}|holderAuthentRelegation=N|holderAuthentStatus=|transactionOrigin=INTERNET|paymentPattern=ONE_SHOT|customerMobilePhone=null|mandateAuthentMethod=null|mandateUsage=null|transactionActors=null|mandateId=null|captureLimitDate=20200408|dccStatus=null|dccResponseCode=null|dccAmount=null|dccCurrencyCode=null|dccExchangeRate=null|dccExchangeRateValidity=null|dccProvider=null|statementReference=SO100x1|panEntryMode=MANUAL|walletType=null|holderAuthentMethod=NO_AUTHENT_METHOD', kind=None),
                                    Constant(value='', kind=None),
                                    Constant(value='HP_2.4', kind=None),
                                    Constant(value='f03f64da6f57c171904d12bf709b1d6d3385131ac914e97a7e1db075ed438f3e', kind=None),
                                    Constant(value='en', kind=None),
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
                                            Constant(value='sips', kind=None),
                                            Name(id='sips_post_data', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='amount',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=314.0, kind=None),
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
                            value=Constant(value='SO100x1', kind=None),
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
                                    Constant(value='sips', kind=None),
                                    Name(id='sips_post_data', ctx=Load()),
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
                                    Constant(value='Sips: validation did not put tx into done state', kind=None),
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
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='reference',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Sips: validation did not update tx id', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='sips_post_data', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='Data', kind=None),
                                    Constant(value='InterfaceVersion', kind=None),
                                    Constant(value='Seal', kind=None),
                                ],
                                values=[
                                    Constant(value='captureDay=0|captureMode=AUTHOR_CAPTURE|currencyCode=840|merchantId=002001000000001|orderChannel=INTERNET|responseCode=12|transactionDateTime=2020-04-08T06:24:08+02:00|transactionReference=SO100x2|keyVersion=1|amount=31400|customerIpAddress=127.0.0.1|returnContext={"return_url": "/payment/process", "reference": "SO100x2"}|paymentPattern=ONE_SHOT|customerMobilePhone=null|mandateAuthentMethod=null|mandateUsage=null|transactionActors=null|mandateId=null|captureLimitDate=null|dccStatus=null|dccResponseCode=null|dccAmount=null|dccCurrencyCode=null|dccExchangeRate=null|dccExchangeRateValidity=null|dccProvider=null|statementReference=SO100x2|panEntryMode=null|walletType=null|holderAuthentMethod=null', kind=None),
                                    Constant(value='HP_2.4', kind=None),
                                    Constant(value='6e1995ea5432580860a04d8515b6eb1507996f97b3c5fa04fb6d9568121a16a2', kind=None),
                                ],
                            ),
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
                            value=Constant(value='SO100x2', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tx2', ctx=Store())],
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
                                    Constant(value='sips', kind=None),
                                    Name(id='sips_post_data', ctx=Load()),
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
                                        value=Name(id='tx2', ctx=Load()),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='cancel', kind=None),
                                    Constant(value='Sips: erroneous validation did not put tx into error state', kind=None),
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
