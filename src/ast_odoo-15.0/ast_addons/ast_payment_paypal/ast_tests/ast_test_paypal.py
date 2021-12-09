Module(
    body=[
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='ValidationError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='mute_logger', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='common',
            names=[alias(name='PaypalCommon', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='controllers.main',
            names=[alias(name='PaypalController', asname=None)],
            level=2,
        ),
        ClassDef(
            name='PaypalForm',
            bases=[Name(id='PaypalCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='_get_expected_values',
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
                                        value=Name(id='PaypalController', ctx=Load()),
                                        attr='_return_url',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='address1', kind=None),
                                    Constant(value='amount', kind=None),
                                    Constant(value='business', kind=None),
                                    Constant(value='cancel_return', kind=None),
                                    Constant(value='city', kind=None),
                                    Constant(value='cmd', kind=None),
                                    Constant(value='country', kind=None),
                                    Constant(value='currency_code', kind=None),
                                    Constant(value='email', kind=None),
                                    Constant(value='first_name', kind=None),
                                    Constant(value='item_name', kind=None),
                                    Constant(value='item_number', kind=None),
                                    Constant(value='last_name', kind=None),
                                    Constant(value='lc', kind=None),
                                    Constant(value='notify_url', kind=None),
                                    Constant(value='return', kind=None),
                                    Constant(value='rm', kind=None),
                                    Constant(value='zip', kind=None),
                                ],
                                values=[
                                    Constant(value='Huge Street 2/543', kind=None),
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
                                            attr='paypal',
                                            ctx=Load(),
                                        ),
                                        attr='paypal_email_account',
                                        ctx=Load(),
                                    ),
                                    Name(id='return_url', ctx=Load()),
                                    Constant(value='Sin City', kind=None),
                                    Constant(value='_xclick', kind=None),
                                    Constant(value='BE', kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='currency',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='norbert.buyer@example.com', kind=None),
                                    Constant(value='Norbert', kind=None),
                                    JoinedStr(
                                        values=[
                                            FormattedValue(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='paypal',
                                                            ctx=Load(),
                                                        ),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value=': ', kind=None),
                                            FormattedValue(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='reference',
                                                    ctx=Load(),
                                                ),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='reference',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Buyer', kind=None),
                                    Constant(value='en_US', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_build_url',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='PaypalController', ctx=Load()),
                                                attr='_notify_url',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='return_url', ctx=Load()),
                                    Constant(value='2', kind=None),
                                    Constant(value='1000', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='paypal',
                                    ctx=Load(),
                                ),
                                attr='fees_active',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='fees', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='currency',
                                                ctx=Load(),
                                            ),
                                            attr='round',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='paypal',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_compute_fees',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='amount',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='currency',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='partner',
                                                            ctx=Load(),
                                                        ),
                                                        attr='country_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='fees', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='handling', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='str', ctx=Load()),
                                                args=[Name(id='fees', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='values', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
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
                                    Constant(value='https://www.sandbox.paypal.com/cgi-bin/webscr', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='expected_values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_expected_values',
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
                                    Constant(value='Paypal: invalid inputs specified in the redirect form.', kind=None),
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
                    name='test_redirect_form_with_fees',
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
                                        attr='paypal',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='fees_active', kind=None),
                                            Constant(value='fees_dom_fixed', kind=None),
                                            Constant(value='fees_dom_var', kind=None),
                                            Constant(value='fees_int_fixed', kind=None),
                                            Constant(value='fees_int_var', kind=None),
                                        ],
                                        values=[
                                            Constant(value=True, kind=None),
                                            Constant(value=1.0, kind=None),
                                            Constant(value=0.35, kind=None),
                                            Constant(value=1.5, kind=None),
                                            Constant(value=0.5, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='expected_values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_expected_values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
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
                                    Constant(value='https://www.sandbox.paypal.com/cgi-bin/webscr', kind=None),
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
                                    Constant(value='Paypal: invalid inputs specified in the redirect form.', kind=None),
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
                            targets=[Name(id='paypal_post_data', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='protection_eligibility', kind=None),
                                    Constant(value='last_name', kind=None),
                                    Constant(value='txn_id', kind=None),
                                    Constant(value='receiver_email', kind=None),
                                    Constant(value='payment_status', kind=None),
                                    Constant(value='payment_gross', kind=None),
                                    Constant(value='tax', kind=None),
                                    Constant(value='residence_country', kind=None),
                                    Constant(value='address_state', kind=None),
                                    Constant(value='payer_status', kind=None),
                                    Constant(value='txn_type', kind=None),
                                    Constant(value='address_street', kind=None),
                                    Constant(value='handling_amount', kind=None),
                                    Constant(value='payment_date', kind=None),
                                    Constant(value='first_name', kind=None),
                                    Constant(value='item_name', kind=None),
                                    Constant(value='address_country', kind=None),
                                    Constant(value='charset', kind=None),
                                    Constant(value='notify_version', kind=None),
                                    Constant(value='address_name', kind=None),
                                    Constant(value='pending_reason', kind=None),
                                    Constant(value='item_number', kind=None),
                                    Constant(value='receiver_id', kind=None),
                                    Constant(value='transaction_subject', kind=None),
                                    Constant(value='business', kind=None),
                                    Constant(value='test_ipn', kind=None),
                                    Constant(value='payer_id', kind=None),
                                    Constant(value='verify_sign', kind=None),
                                    Constant(value='address_zip', kind=None),
                                    Constant(value='address_country_code', kind=None),
                                    Constant(value='address_city', kind=None),
                                    Constant(value='address_status', kind=None),
                                    Constant(value='mc_currency', kind=None),
                                    Constant(value='shipping', kind=None),
                                    Constant(value='payer_email', kind=None),
                                    Constant(value='payment_type', kind=None),
                                    Constant(value='mc_gross', kind=None),
                                    Constant(value='ipn_track_id', kind=None),
                                    Constant(value='quantity', kind=None),
                                ],
                                values=[
                                    Constant(value='Ineligible', kind='u'),
                                    Constant(value='Poilu', kind='u'),
                                    Constant(value='08D73520KX778924N', kind='u'),
                                    Constant(value='dummy', kind=None),
                                    Constant(value='Pending', kind='u'),
                                    Constant(value='', kind='u'),
                                    Constant(value='0.00', kind='u'),
                                    Constant(value='FR', kind='u'),
                                    Constant(value='Alsace', kind='u'),
                                    Constant(value='verified', kind='u'),
                                    Constant(value='web_accept', kind='u'),
                                    Constant(value='Av. de la Pelouse, 87648672 Mayet', kind='u'),
                                    Constant(value='0.00', kind='u'),
                                    Constant(value='03:21:19 Nov 18, 2013 PST', kind='u'),
                                    Constant(value='Norbert', kind='u'),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='reference',
                                        ctx=Load(),
                                    ),
                                    Constant(value='France', kind='u'),
                                    Constant(value='windows-1252', kind='u'),
                                    Constant(value='3.7', kind='u'),
                                    Constant(value='Norbert Poilu', kind='u'),
                                    Constant(value='multi_currency', kind='u'),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='reference',
                                        ctx=Load(),
                                    ),
                                    Constant(value='dummy', kind='u'),
                                    Constant(value='', kind='u'),
                                    Constant(value='dummy', kind='u'),
                                    Constant(value='1', kind='u'),
                                    Constant(value='VTDKRZQSAHYPS', kind='u'),
                                    Constant(value='An5ns1Kso7MWUdW4ErQKJJJ4qi4-AVoiUf-3478q3vrSmqh08IouiYpM', kind='u'),
                                    Constant(value='75002', kind='u'),
                                    Constant(value='FR', kind='u'),
                                    Constant(value='Paris', kind='u'),
                                    Constant(value='unconfirmed', kind='u'),
                                    Constant(value='EUR', kind='u'),
                                    Constant(value='0.00', kind='u'),
                                    Constant(value='tde+buyer@odoo.com', kind='u'),
                                    Constant(value='instant', kind='u'),
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
                                    Constant(value='866df2ccd444b', kind='u'),
                                    Constant(value='1', kind='u'),
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
                                            Constant(value='paypal', kind=None),
                                            Name(id='paypal_post_data', ctx=Load()),
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
                                    Constant(value='paypal', kind=None),
                                    Name(id='paypal_post_data', ctx=Load()),
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
                                    Constant(value='paypal: wrong state after receiving a valid pending notification', kind=None),
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
                                    Constant(value='multi_currency', kind=None),
                                    Constant(value='paypal: wrong state message after receiving a valid pending notification', kind=None),
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
                                    Constant(value='08D73520KX778924N', kind=None),
                                    Constant(value='paypal: wrong txn_id after receiving a valid pending notification', kind=None),
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
                                    value=Name(id='paypal_post_data', ctx=Load()),
                                    slice=Constant(value='payment_status', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='Completed', kind=None),
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
                                    Constant(value='paypal', kind=None),
                                    Name(id='paypal_post_data', ctx=Load()),
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
                                    Constant(value='paypal: wrong state after receiving a valid pending notification', kind=None),
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
                                    Constant(value='08D73520KX778924N', kind=None),
                                    Constant(value='paypal: wrong txn_id after receiving a valid pending notification', kind=None),
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
                    name='test_fees_computation',
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
                                        attr='paypal',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='fees_active', kind=None),
                                            Constant(value='fees_int_fixed', kind=None),
                                            Constant(value='fees_int_var', kind=None),
                                        ],
                                        values=[
                                            Constant(value=True, kind=None),
                                            Constant(value=0.3, kind=None),
                                            Constant(value=2.9, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='total_fee', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='paypal',
                                        ctx=Load(),
                                    ),
                                    attr='_compute_fees',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=100, kind=None),
                                    Constant(value=False, kind=None),
                                    Constant(value=False, kind=None),
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
                                    Call(
                                        func=Name(id='round', ctx=Load()),
                                        args=[
                                            Name(id='total_fee', ctx=Load()),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=3.3, kind=None),
                                    Constant(value='Wrong computation of the Paypal fees', kind=None),
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
