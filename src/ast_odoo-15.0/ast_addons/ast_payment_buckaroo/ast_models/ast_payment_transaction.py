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
            module='odoo.addons.payment_buckaroo.const',
            names=[alias(name='STATUS_CODES_MAPPING', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.payment_buckaroo.controllers.main',
            names=[alias(name='BuckarooController', asname=None)],
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
        FunctionDef(
            name='_normalize_dataset',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='data', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Set all keys of a dictionary to uppercase.\n\n    As Buckaroo parameters names are case insensitive, we can convert everything to upper case to\n    easily detected the presence of a parameter by checking the uppercase key only.\n\n    :param dict data: The dictionary whose keys must be set to uppercase\n    :return: A copy of the original data with all keys set to uppercase\n    :rtype: dict\n    ', kind=None),
                ),
                Return(
                    value=DictComp(
                        key=Call(
                            func=Attribute(
                                value=Name(id='key', ctx=Load()),
                                attr='upper',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[],
                        ),
                        value=Name(id='val', ctx=Load()),
                        generators=[
                            comprehension(
                                target=Tuple(
                                    elts=[
                                        Name(id='key', ctx=Store()),
                                        Name(id='val', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                                iter=Call(
                                    func=Attribute(
                                        value=Name(id='data', ctx=Load()),
                                        attr='items',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ifs=[],
                                is_async=0,
                            ),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
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
                            value=Constant(value=' Override of payment to return Buckaroo-specific rendering values.\n\n        Note: self.ensure_one() from `_get_processing_values`\n\n        :param dict processing_values: The generic and specific processing values of the transaction\n        :return: The dict of acquirer-specific processing values\n        :rtype: dict\n        ', kind=None),
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
                                comparators=[Constant(value='buckaroo', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Name(id='res', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='return_url', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='urls', ctx=Load()),
                                    attr='url_join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='acquirer_id',
                                                ctx=Load(),
                                            ),
                                            attr='get_base_url',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
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
                            targets=[Name(id='rendering_values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='api_url', kind=None),
                                    Constant(value='Brq_websitekey', kind=None),
                                    Constant(value='Brq_amount', kind=None),
                                    Constant(value='Brq_currency', kind=None),
                                    Constant(value='Brq_invoicenumber', kind=None),
                                    Constant(value='Brq_return', kind=None),
                                    Constant(value='Brq_returncancel', kind=None),
                                    Constant(value='Brq_returnerror', kind=None),
                                    Constant(value='Brq_returnreject', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='acquirer_id',
                                                ctx=Load(),
                                            ),
                                            attr='_buckaroo_get_api_url',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='acquirer_id',
                                            ctx=Load(),
                                        ),
                                        attr='buckaroo_website_key',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
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
                                        value=Name(id='self', ctx=Load()),
                                        attr='reference',
                                        ctx=Load(),
                                    ),
                                    Name(id='return_url', ctx=Load()),
                                    Name(id='return_url', ctx=Load()),
                                    Name(id='return_url', ctx=Load()),
                                    Name(id='return_url', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='partner_lang',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='rendering_values', ctx=Load()),
                                            slice=Constant(value='Brq_culture', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='partner_lang',
                                                ctx=Load(),
                                            ),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='_', kind=None),
                                            Constant(value='-', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='rendering_values', ctx=Load()),
                                    slice=Constant(value='Brq_signature', kind=None),
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
                                    attr='_buckaroo_generate_digital_sign',
                                    ctx=Load(),
                                ),
                                args=[Name(id='rendering_values', ctx=Load())],
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
                            value=Name(id='rendering_values', ctx=Load()),
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
                            value=Constant(value=' Override of payment to find the transaction based on Buckaroo data.\n\n        :param str provider: The provider of the acquirer that handled the transaction\n        :param dict data: The feedback data sent by the provider\n        :return: The transaction if found\n        :rtype: recordset of `payment.transaction`\n        :raise: ValidationError if inconsistent data were received\n        :raise: ValidationError if the data match no transaction\n        :raise: ValidationError if the signature can not be verified\n        ', kind=None),
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
                                comparators=[Constant(value='buckaroo', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Name(id='tx', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='normalized_data', ctx=Store())],
                            value=Call(
                                func=Name(id='_normalize_dataset', ctx=Load()),
                                args=[Name(id='data', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='reference', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='normalized_data', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='BRQ_INVOICENUMBER', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='shasign', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='normalized_data', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='BRQ_SIGNATURE', kind=None)],
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
                                        operand=Name(id='shasign', ctx=Load()),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValidationError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='Buckaroo: ', kind=None),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Received data with missing reference (%(ref)s) or shasign (%(sign))', kind=None)],
                                                    keywords=[
                                                        keyword(
                                                            arg='ref',
                                                            value=Name(id='reference', ctx=Load()),
                                                        ),
                                                        keyword(
                                                            arg='sign',
                                                            value=Name(id='shasign', ctx=Load()),
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
                                                    Constant(value='buckaroo', kind=None),
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
                                                left=Constant(value='Buckaroo: ', kind=None),
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
                            targets=[Name(id='shasign_check', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='tx', ctx=Load()),
                                        attr='acquirer_id',
                                        ctx=Load(),
                                    ),
                                    attr='_buckaroo_generate_digital_sign',
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
                                left=Name(id='shasign_check', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[Name(id='shasign', ctx=Load())],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValidationError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='Buckaroo: ', kind=None),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Invalid shasign: received %(sign)s, computed %(check)s', kind=None)],
                                                    keywords=[
                                                        keyword(
                                                            arg='sign',
                                                            value=Name(id='shasign', ctx=Load()),
                                                        ),
                                                        keyword(
                                                            arg='check',
                                                            value=Name(id='shasign_check', ctx=Load()),
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
                            value=Constant(value=' Override of payment to process the transaction based on Buckaroo data.\n\n        Note: self.ensure_one()\n\n        :param dict data: The feedback data sent by the provider\n        :return: None\n        :raise: ValidationError if inconsistent data were received\n        ', kind=None),
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
                                comparators=[Constant(value='buckaroo', kind=None)],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='normalized_data', ctx=Store())],
                            value=Call(
                                func=Name(id='_normalize_dataset', ctx=Load()),
                                args=[Name(id='data', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='transaction_keys', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='normalized_data', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='BRQ_TRANSACTIONS', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='transaction_keys', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValidationError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='Buckaroo: ', kind=None),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Received data with missing transaction keys', kind=None)],
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='acquirer_reference',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='transaction_keys', ctx=Load()),
                                        attr='split',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value=',', kind=None)],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='status_code', ctx=Store())],
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='normalized_data', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='BRQ_STATUSCODE', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value=0, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='status_code', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Subscript(
                                        value=Name(id='STATUS_CODES_MAPPING', ctx=Load()),
                                        slice=Constant(value='pending', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
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
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='status_code', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Subscript(
                                                value=Name(id='STATUS_CODES_MAPPING', ctx=Load()),
                                                slice=Constant(value='done', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
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
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='status_code', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Subscript(
                                                        value=Name(id='STATUS_CODES_MAPPING', ctx=Load()),
                                                        slice=Constant(value='cancel', kind=None),
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
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='status_code', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[
                                                            Subscript(
                                                                value=Name(id='STATUS_CODES_MAPPING', ctx=Load()),
                                                                slice=Constant(value='refused', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_set_error',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[
                                                                            Constant(value='Your payment was refused (code %s). Please try again.', kind=None),
                                                                            Name(id='status_code', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='status_code', ctx=Load()),
                                                                ops=[In()],
                                                                comparators=[
                                                                    Subscript(
                                                                        value=Name(id='STATUS_CODES_MAPPING', ctx=Load()),
                                                                        slice=Constant(value='error', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='_set_error',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Call(
                                                                                func=Name(id='_', ctx=Load()),
                                                                                args=[
                                                                                    Constant(value='An error occured during processing of your payment (code %s). Please try again.', kind=None),
                                                                                    Name(id='status_code', ctx=Load()),
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
                                                                            value=Name(id='_logger', ctx=Load()),
                                                                            attr='warning',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Constant(value='Buckaroo: received unknown status code: %s', kind=None),
                                                                            Name(id='status_code', ctx=Load()),
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
                                                                                left=Constant(value='Buckaroo: ', kind=None),
                                                                                op=Add(),
                                                                                right=Call(
                                                                                    func=Name(id='_', ctx=Load()),
                                                                                    args=[
                                                                                        Constant(value='Unknown status code: %s', kind=None),
                                                                                        Name(id='status_code', ctx=Load()),
                                                                                    ],
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
