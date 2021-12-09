Module(
    body=[
        Import(
            names=[alias(name='json', asname=None)],
        ),
        ImportFrom(
            module='uuid',
            names=[alias(name='uuid4', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='lxml',
            names=[
                alias(name='etree', asname=None),
                alias(name='objectify', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='http', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='HttpCase', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.payment.tests.utils',
            names=[alias(name='PaymentTestUtils', asname=None)],
            level=0,
        ),
        ClassDef(
            name='PaymentHttpCommon',
            bases=[
                Name(id='PaymentTestUtils', ctx=Load()),
                Name(id='HttpCase', ctx=Load()),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=" HttpCase common to build and simulate requests going through payment controllers.\n\n    Only use if you effectively want to test controllers.\n    If you only want to test 'models' code, the PaymentCommon should be sufficient.\n\n    Note: This Common is expected to be used in parallel with the main PaymentCommon.\n    ", kind=None),
                ),
                FunctionDef(
                    name='_build_jsonrpc_payload',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='params', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Helper to properly build jsonrpc payload', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='getattr', ctx=Load()),
                                    args=[
                                        Name(id='self', ctx=Load()),
                                        Constant(value='session', kind=None),
                                        Constant(value=None, kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='authenticate',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='', kind=None),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='params', ctx=Load()),
                                    slice=Constant(value='csrf_token', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='http', ctx=Load()),
                                        attr='WebRequest',
                                        ctx=Load(),
                                    ),
                                    attr='csrf_token',
                                    ctx=Load(),
                                ),
                                args=[Name(id='self', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='jsonrpc', kind=None),
                                    Constant(value='method', kind=None),
                                    Constant(value='id', kind=None),
                                    Constant(value='params', kind=None),
                                ],
                                values=[
                                    Constant(value='2.0', kind=None),
                                    Constant(value='call', kind=None),
                                    Call(
                                        func=Name(id='str', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='uuid4', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='params', ctx=Load()),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_make_http_get_request',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='url', annotation=None, type_comment=None),
                            arg(arg='params', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='formatted_data', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='k', ctx=Store()),
                                    Name(id='v', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='params', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='v', ctx=Load()),
                                            Name(id='float', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='formatted_data', ctx=Load()),
                                                    slice=Name(id='k', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='str', ctx=Load()),
                                                args=[Name(id='v', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='formatted_data', ctx=Load()),
                                                    slice=Name(id='k', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='v', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='opener',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Name(id='url', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='params',
                                        value=Name(id='formatted_data', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_make_json_request',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='url', annotation=None, type_comment=None),
                            arg(arg='params', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_build_jsonrpc_payload',
                                    ctx=Load(),
                                ),
                                args=[Name(id='params', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='opener',
                                        ctx=Load(),
                                    ),
                                    attr='post',
                                    ctx=Load(),
                                ),
                                args=[Name(id='url', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='json',
                                        value=Name(id='data', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_tx_context',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='response', annotation=None, type_comment=None),
                            arg(arg='form_name', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Extracts txContext & other form info (acquirer & token ids)\n        from a payment response (with manage/checkout html form)\n\n        :param response: http Response, with a payment form as text\n        :param str form_name: o_payment_manage / o_payment_checkout\n        :return: Transaction context (+ acquirer_ids & token_ids)\n        :rtype: dict\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='html_tree', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='objectify', ctx=Load()),
                                    attr='fromstring',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='response', ctx=Load()),
                                        attr='text',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='parser',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='etree', ctx=Load()),
                                                attr='HTMLParser',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='checkout_form', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='html_tree', ctx=Load()),
                                        attr='xpath',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        JoinedStr(
                                            values=[
                                                Constant(value="//form[@name='", kind=None),
                                                FormattedValue(
                                                    value=Name(id='form_name', ctx=Load()),
                                                    conversion=-1,
                                                    format_spec=None,
                                                ),
                                                Constant(value="']", kind=None),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='key', ctx=Store()),
                                    Name(id='val', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='checkout_form', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='key', ctx=Load()),
                                            attr='startswith',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='data-', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='formatted_key', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='key', ctx=Load()),
                                                        slice=Slice(
                                                            lower=Constant(value=5, kind=None),
                                                            upper=None,
                                                            step=None,
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='-', kind=None),
                                                    Constant(value='_', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='formatted_key', ctx=Load()),
                                                    attr='endswith',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='_id', kind=None)],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='formatted_val', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[Name(id='val', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='formatted_key', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='amount', kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='formatted_val', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='float', ctx=Load()),
                                                                args=[Name(id='val', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[Name(id='formatted_val', ctx=Store())],
                                                            value=Name(id='val', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Name(id='formatted_key', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='formatted_val', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='payment_options_inputs', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='html_tree', ctx=Load()),
                                    attr='xpath',
                                    ctx=Load(),
                                ),
                                args=[Constant(value="//input[@name='o_payment_radio']", kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='acquirer_ids', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='token_ids', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='p_o_input', ctx=Store()),
                            iter=Name(id='payment_options_inputs', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='data', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='key', ctx=Store()),
                                            Name(id='val', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='p_o_input', ctx=Load()),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='key', ctx=Load()),
                                                    attr='startswith',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='data-', kind=None)],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='data', ctx=Load()),
                                                            slice=Subscript(
                                                                value=Name(id='key', ctx=Load()),
                                                                slice=Slice(
                                                                    lower=Constant(value=5, kind=None),
                                                                    upper=None,
                                                                    step=None,
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='val', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='data', ctx=Load()),
                                            slice=Constant(value='payment-option-type', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='acquirer', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='acquirer_ids', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='data', ctx=Load()),
                                                                slice=Constant(value='payment-option-id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='token_ids', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='data', ctx=Load()),
                                                                slice=Constant(value='payment-option-id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='acquirer_ids', kind=None),
                                            Constant(value='token_ids', kind=None),
                                        ],
                                        values=[
                                            Name(id='acquirer_ids', ctx=Load()),
                                            Name(id='token_ids', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
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
                    name='_prepare_pay_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='amount', annotation=None, type_comment=None),
                            arg(arg='currency', annotation=None, type_comment=None),
                            arg(arg='reference', annotation=None, type_comment=None),
                            arg(arg='partner', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=0.0, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value='', kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Prepare basic payment/pay route values\n\n        NOTE: needs PaymentCommon to enable fallback values.\n\n        :rtype: dict\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='amount', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='amount', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='currency', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='currency', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='currency',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='reference', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='reference', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='reference',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partner', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='partner', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='partner',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='amount', kind=None),
                                    Constant(value='currency_id', kind=None),
                                    Constant(value='reference', kind=None),
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='access_token', kind=None),
                                ],
                                values=[
                                    Name(id='amount', ctx=Load()),
                                    Attribute(
                                        value=Name(id='currency', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='reference', ctx=Load()),
                                    Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_generate_test_access_token',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Name(id='amount', ctx=Load()),
                                            Attribute(
                                                value=Name(id='currency', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='portal_pay',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='route_kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='/payment/pay txContext feedback\n\n        NOTE: must be authenticated before calling method.\n        Or an access_token should be specified in route_kwargs\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='uri', ctx=Store())],
                            value=Constant(value='/payment/pay', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='url', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_build_url',
                                    ctx=Load(),
                                ),
                                args=[Name(id='uri', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_make_http_get_request',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='url', ctx=Load()),
                                    Name(id='route_kwargs', ctx=Load()),
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
                    name='get_tx_checkout_context',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='route_kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='portal_pay',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='route_kwargs', ctx=Load()),
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
                                        value=Name(id='response', ctx=Load()),
                                        attr='status_code',
                                        ctx=Load(),
                                    ),
                                    Constant(value=200, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_tx_context',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='response', ctx=Load()),
                                    Constant(value='o_payment_checkout', kind=None),
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
                    name='portal_payment_method',
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
                            value=Constant(value='/my/payment_method txContext feedback\n\n        NOTE: must be authenticated before calling method\n            validation flow is restricted to logged users\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='uri', ctx=Store())],
                            value=Constant(value='/my/payment_method', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='url', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_build_url',
                                    ctx=Load(),
                                ),
                                args=[Name(id='uri', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_make_http_get_request',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='url', ctx=Load()),
                                    Dict(keys=[], values=[]),
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
                    name='get_tx_manage_context',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='route_kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='portal_payment_method',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='route_kwargs', ctx=Load()),
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
                                        value=Name(id='response', ctx=Load()),
                                        attr='status_code',
                                        ctx=Load(),
                                    ),
                                    Constant(value=200, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_tx_context',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='response', ctx=Load()),
                                    Constant(value='o_payment_manage', kind=None),
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
                    name='portal_transaction',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='route_kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='/payment/transaction feedback\n\n        :returns: processing values for given route_kwargs\n        :rtype: dict\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='uri', ctx=Store())],
                            value=Constant(value='/payment/transaction', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='url', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_build_url',
                                    ctx=Load(),
                                ),
                                args=[Name(id='uri', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_make_json_request',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='url', ctx=Load()),
                                    Name(id='route_kwargs', ctx=Load()),
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
                    name='get_processing_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='route_kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='portal_transaction',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='route_kwargs', ctx=Load()),
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
                                        value=Name(id='response', ctx=Load()),
                                        attr='status_code',
                                        ctx=Load(),
                                    ),
                                    Constant(value=200, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='resp_content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='json', ctx=Load()),
                                    attr='loads',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='response', ctx=Load()),
                                        attr='content',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Subscript(
                                value=Name(id='resp_content', ctx=Load()),
                                slice=Constant(value='result', kind=None),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
