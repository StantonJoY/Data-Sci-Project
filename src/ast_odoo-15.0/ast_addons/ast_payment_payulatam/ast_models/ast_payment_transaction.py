Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='werkzeug',
            names=[alias(name='urls', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='api', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='ValidationError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.float_utils',
            names=[alias(name='float_repr', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.payment',
            names=[alias(name='utils', asname='payment_utils')],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.payment_payulatam.controllers.main',
            names=[alias(name='PayuLatamController', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='PaymentTransaction',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='payment.transaction', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_reference',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='provider', annotation=None, type_comment=None),
                            arg(arg='prefix', annotation=None, type_comment=None),
                            arg(arg='separator', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value='-', kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Override of payment to ensure that PayU Latam requirements for references are satisfied.\n\n        PayU Latam requirements for transaction are as follows:\n        - References must be unique at provider level for a given merchant account.\n          This is satisfied by singularizing the prefix with the current datetime. If two\n          transactions are created simultaneously, `_compute_reference` ensures the uniqueness of\n          references by suffixing a sequence number.\n\n        :param str provider: The provider of the acquirer handling the transaction\n        :param str prefix: The custom prefix used to compute the full reference\n        :param str separator: The custom separator used to separate the prefix from the suffix\n        :return: The unique reference for the transaction\n        :rtype: str\n        ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='provider', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='payulatam', kind=None)],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='prefix', ctx=Load()),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='prefix', ctx=Store())],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='sudo',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            attr='_compute_reference_prefix',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='provider', ctx=Load()),
                                                            Name(id='separator', ctx=Load()),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg=None,
                                                                value=Name(id='kwargs', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    Constant(value=None, kind=None),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='prefix', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='payment_utils', ctx=Load()),
                                            attr='singularize_reference_prefix',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='prefix',
                                                value=Name(id='prefix', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='separator',
                                                value=Name(id='separator', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_compute_reference',
                                    ctx=Load(),
                                ),
                                args=[Name(id='provider', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='prefix',
                                        value=Name(id='prefix', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='separator',
                                        value=Name(id='separator', ctx=Load()),
                                    ),
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_specific_rendering_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='processing_values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Override of payment to return Payulatam-specific rendering values.\n\n        Note: self.ensure_one() from `_get_processing_values`\n\n        :param dict processing_values: The generic and specific processing values of the transaction\n        :return: The dict of acquirer-specific processing values\n        :rtype: dict\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_specific_rendering_values',
                                    ctx=Load(),
                                ),
                                args=[Name(id='processing_values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='provider',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='payulatam', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Name(id='res', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='api_url', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='acquirer_id',
                                            ctx=Load(),
                                        ),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    ops=[Eq()],
                                    comparators=[Constant(value='enabled', kind=None)],
                                ),
                                body=Constant(value='https://checkout.payulatam.com/ppp-web-gateway-payu/', kind=None),
                                orelse=Constant(value='https://sandbox.checkout.payulatam.com/ppp-web-gateway-payu/', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='payulatam_values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='merchantId', kind=None),
                                    Constant(value='referenceCode', kind=None),
                                    Constant(value='description', kind=None),
                                    Constant(value='amount', kind=None),
                                    Constant(value='tax', kind=None),
                                    Constant(value='taxReturnBase', kind=None),
                                    Constant(value='currency', kind=None),
                                    Constant(value='accountId', kind=None),
                                    Constant(value='buyerFullName', kind=None),
                                    Constant(value='buyerEmail', kind=None),
                                    Constant(value='responseUrl', kind=None),
                                    Constant(value='api_url', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='acquirer_id',
                                            ctx=Load(),
                                        ),
                                        attr='payulatam_merchant_id',
                                        ctx=Load(),
                                    ),
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
                                        func=Name(id='float_repr', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='processing_values', ctx=Load()),
                                                slice=Constant(value='amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='currency_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='decimal_places',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=2, kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='currency_id',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='acquirer_id',
                                            ctx=Load(),
                                        ),
                                        attr='payulatam_account_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='partner_name',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='partner_email',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='urls', ctx=Load()),
                                            attr='url_join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='get_base_url',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Name(id='PayuLatamController', ctx=Load()),
                                                attr='_return_url',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='api_url', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='acquirer_id',
                                        ctx=Load(),
                                    ),
                                    attr='state',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='enabled', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='payulatam_values', ctx=Load()),
                                            slice=Constant(value='test', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=1, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='payulatam_values', ctx=Load()),
                                    slice=Constant(value='signature', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='acquirer_id',
                                        ctx=Load(),
                                    ),
                                    attr='_payulatam_generate_sign',
                                    ctx=Load(),
                                ),
                                args=[Name(id='payulatam_values', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='incoming',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='payulatam_values', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_tx_from_feedback_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='provider', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Override of payment to find the transaction based on Payulatam data.\n\n        :param str provider: The provider of the acquirer that handled the transaction\n        :param dict data: The feedback data sent by the provider\n        :return: The transaction if found\n        :rtype: recordset of `payment.transaction`\n        :raise: ValidationError if inconsistent data were received\n        :raise: ValidationError if the data match no transaction\n        :raise: ValidationError if the signature can not be verified\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='tx', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_tx_from_feedback_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='provider', ctx=Load()),
                                    Name(id='data', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='provider', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[Constant(value='payulatam', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Name(id='tx', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='reference', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='data', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='referenceCode', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sign', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='data', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='signature', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='reference', ctx=Load()),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='sign', ctx=Load()),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValidationError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='PayU Latam: ', kind=None),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Received data with missing reference (%(ref)s) or sign (%(sign)s).', kind=None)],
                                                    keywords=[
                                                        keyword(
                                                            arg='ref',
                                                            value=Name(id='reference', ctx=Load()),
                                                        ),
                                                        keyword(
                                                            arg='sign',
                                                            value=Name(id='sign', ctx=Load()),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='tx', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='reference', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='reference', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='provider', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='payulatam', kind=None),
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='tx', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValidationError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='PayU Latam: ', kind=None),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[
                                                        Constant(value='No transaction found matching reference %s.', kind=None),
                                                        Name(id='reference', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='sign_check', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='tx', ctx=Load()),
                                        attr='acquirer_id',
                                        ctx=Load(),
                                    ),
                                    attr='_payulatam_generate_sign',
                                    ctx=Load(),
                                ),
                                args=[Name(id='data', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='incoming',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='sign_check', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[Name(id='sign', ctx=Load())],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValidationError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='PayU Latam: ', kind=None),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Invalid sign: received %(sign)s, computed %(check)s.', kind=None)],
                                                    keywords=[
                                                        keyword(
                                                            arg='sign',
                                                            value=Name(id='sign', ctx=Load()),
                                                        ),
                                                        keyword(
                                                            arg='check',
                                                            value=Name(id='sign_check', ctx=Load()),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='tx', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_process_feedback_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Override of payment to process the transaction based on Payulatam data.\n\n        Note: self.ensure_one()\n\n        :param dict data: The feedback data sent by the provider\n        :return: None\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_process_feedback_data',
                                    ctx=Load(),
                                ),
                                args=[Name(id='data', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='provider',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='payulatam', kind=None)],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='acquirer_reference',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='data', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='transactionId', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='status', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='data', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='lapTransactionState', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='state_message', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='data', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='message', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='status', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='PENDING', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_set_pending',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='state_message',
                                                value=Name(id='state_message', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='status', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='APPROVED', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_set_done',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='state_message',
                                                        value=Name(id='state_message', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='status', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='EXPIRED', kind=None),
                                                            Constant(value='DECLINED', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_set_canceled',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='state_message',
                                                                value=Name(id='state_message', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='warning',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='received unrecognized payment state %s for transaction with reference %s', kind=None),
                                                            Name(id='status', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='reference',
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
                                                            attr='_set_error',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='PayU Latam: ', kind=None),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='_', ctx=Load()),
                                                                    args=[Constant(value='Invalid payment status.', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
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
