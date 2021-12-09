Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='pprint', asname=None)],
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
            names=[
                alias(name='UserError', asname=None),
                alias(name='ValidationError', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module=None,
            names=[alias(name='const', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='odoo.addons.payment',
            names=[alias(name='utils', asname='payment_utils')],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.payment_ogone.controllers.main',
            names=[alias(name='OgoneController', asname=None)],
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
                            value=Constant(value=' Override of payment to ensure that Ogone requirements for references are satisfied.\n\n        Ogone requirements for references are as follows:\n        - References must be unique at provider level for a given merchant account.\n          This is satisfied by singularizing the prefix with the current datetime. If two\n          transactions are created simultaneously, `_compute_reference` ensures the uniqueness of\n          references by suffixing a sequence number.\n\n        :param str provider: The provider of the acquirer handling the transaction\n        :param str prefix: The custom prefix used to compute the full reference\n        :param str separator: The custom separator used to separate the prefix from the suffix\n        :return: The unique reference for the transaction\n        :rtype: str\n        ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='provider', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[Constant(value='ogone', kind=None)],
                            ),
                            body=[
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
                                                arg=None,
                                                value=Name(id='kwargs', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
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
                                        arg='max_length',
                                        value=Constant(value=40, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
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
                            value=Constant(value=' Override of payment to return Ogone-specific rendering values.\n\n        Note: self.ensure_one() from `_get_processing_values`\n\n        :param dict processing_values: The generic and specific processing values of the transaction\n        :return: The dict of acquirer-specific processing values\n        :rtype: dict\n        ', kind=None),
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='acquirer_id',
                                        ctx=Load(),
                                    ),
                                    attr='provider',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='ogone', kind=None)],
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
                                        value=Name(id='OgoneController', ctx=Load()),
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
                                    Constant(value='PSPID', kind=None),
                                    Constant(value='ORDERID', kind=None),
                                    Constant(value='AMOUNT', kind=None),
                                    Constant(value='CURRENCY', kind=None),
                                    Constant(value='LANGUAGE', kind=None),
                                    Constant(value='EMAIL', kind=None),
                                    Constant(value='OWNERADDRESS', kind=None),
                                    Constant(value='OWNERZIP', kind=None),
                                    Constant(value='OWNERTOWN', kind=None),
                                    Constant(value='OWNERCTY', kind=None),
                                    Constant(value='OWNERTELNO', kind=None),
                                    Constant(value='OPERATION', kind=None),
                                    Constant(value='USERID', kind=None),
                                    Constant(value='ACCEPTURL', kind=None),
                                    Constant(value='DECLINEURL', kind=None),
                                    Constant(value='EXCEPTIONURL', kind=None),
                                    Constant(value='CANCELURL', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='acquirer_id',
                                            ctx=Load(),
                                        ),
                                        attr='ogone_pspid',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='reference',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='payment_utils', ctx=Load()),
                                            attr='to_minor_currency_units',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='amount',
                                                ctx=Load(),
                                            ),
                                            Constant(value=None, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
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
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='partner_lang',
                                                ctx=Load(),
                                            ),
                                            Constant(value='en_US', kind=None),
                                        ],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='partner_email',
                                                ctx=Load(),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='partner_address',
                                                ctx=Load(),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='partner_zip',
                                                ctx=Load(),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='partner_city',
                                                ctx=Load(),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='partner_country_id',
                                                    ctx=Load(),
                                                ),
                                                attr='code',
                                                ctx=Load(),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='partner_phone',
                                                ctx=Load(),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                    Constant(value='SAL', kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='acquirer_id',
                                            ctx=Load(),
                                        ),
                                        attr='ogone_userid',
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
                                attr='tokenize',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rendering_values', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='ALIAS', kind=None),
                                                    Constant(value='ALIASUSAGE', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='payment_utils', ctx=Load()),
                                                            attr='singularize_reference_prefix',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='prefix',
                                                                value=Constant(value='ODOO-ALIAS', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Storing your payment details is necessary for future use.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='rendering_values', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='SHASIGN', kind=None),
                                            Constant(value='api_url', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='acquirer_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_ogone_generate_signature',
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
                                                    attr='upper',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='acquirer_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_ogone_get_api_url',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='hosted_payment_page', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
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
                    name='_send_payment_request',
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
                            value=Constant(value=' Override of payment to send a payment request to Ogone.\n\n        Note: self.ensure_one()\n\n        :return: None\n        :raise: UserError if the transaction is not linked to a token\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_send_payment_request',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                comparators=[Constant(value='ogone', kind=None)],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='token_id',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='Ogone: ', kind=None),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='The transaction is not linked to a token.', kind=None)],
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
                            targets=[Name(id='base_url', ctx=Store())],
                            value=Call(
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='PSPID', kind=None),
                                    Constant(value='ORDERID', kind=None),
                                    Constant(value='USERID', kind=None),
                                    Constant(value='PSWD', kind=None),
                                    Constant(value='AMOUNT', kind=None),
                                    Constant(value='CURRENCY', kind=None),
                                    Constant(value='CN', kind=None),
                                    Constant(value='EMAIL', kind=None),
                                    Constant(value='OWNERADDRESS', kind=None),
                                    Constant(value='OWNERZIP', kind=None),
                                    Constant(value='OWNERTOWN', kind=None),
                                    Constant(value='OWNERCTY', kind=None),
                                    Constant(value='OWNERTELNO', kind=None),
                                    Constant(value='OPERATION', kind=None),
                                    Constant(value='ALIAS', kind=None),
                                    Constant(value='ALIASPERSISTEDAFTERUSE', kind=None),
                                    Constant(value='ECI', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='acquirer_id',
                                            ctx=Load(),
                                        ),
                                        attr='ogone_pspid',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='reference',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='acquirer_id',
                                            ctx=Load(),
                                        ),
                                        attr='ogone_userid',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='acquirer_id',
                                            ctx=Load(),
                                        ),
                                        attr='ogone_password',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='payment_utils', ctx=Load()),
                                            attr='to_minor_currency_units',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='amount',
                                                ctx=Load(),
                                            ),
                                            Constant(value=None, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
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
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='partner_name',
                                                ctx=Load(),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='partner_email',
                                                ctx=Load(),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='partner_address',
                                                ctx=Load(),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='partner_zip',
                                                ctx=Load(),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='partner_city',
                                                ctx=Load(),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='partner_country_id',
                                                    ctx=Load(),
                                                ),
                                                attr='code',
                                                ctx=Load(),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='partner_phone',
                                                ctx=Load(),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                    Constant(value='SAL', kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='token_id',
                                            ctx=Load(),
                                        ),
                                        attr='acquirer_ref',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Y', kind=None),
                                    Constant(value=9, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='data', ctx=Load()),
                                    slice=Constant(value='SHASIGN', kind=None),
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
                                    attr='_ogone_generate_signature',
                                    ctx=Load(),
                                ),
                                args=[Name(id='data', ctx=Load())],
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
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='making payment request:\n%s', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='pprint', ctx=Load()),
                                            attr='pformat',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            DictComp(
                                                key=Name(id='k', ctx=Load()),
                                                value=Name(id='v', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=Tuple(
                                                            elts=[
                                                                Name(id='k', ctx=Store()),
                                                                Name(id='v', ctx=Store()),
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
                                                        ifs=[
                                                            Compare(
                                                                left=Name(id='k', ctx=Load()),
                                                                ops=[NotEq()],
                                                                comparators=[Constant(value='PSWD', kind=None)],
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='response_content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='acquirer_id',
                                        ctx=Load(),
                                    ),
                                    attr='_ogone_make_request',
                                    ctx=Load(),
                                ),
                                args=[Name(id='data', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='tree', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='objectify', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='response_content', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='etree', ctx=Load()),
                                        attr='XMLSyntaxError',
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValidationError', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='Ogone: ', kind=None),
                                                        op=Add(),
                                                        right=Constant(value='Received badly structured response from the API.', kind=None),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='received payment request response as an etree:\n%s', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='tostring',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='tree', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='pretty_print',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='encoding',
                                                value=Constant(value='utf-8', kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='feedback_data', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='ORDERID', kind=None),
                                    Constant(value='tree', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tree', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='orderID', kind=None)],
                                        keywords=[],
                                    ),
                                    Name(id='tree', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='entering _handle_feedback_data with data:\n%s', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='pprint', ctx=Load()),
                                            attr='pformat',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='feedback_data', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_handle_feedback_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='ogone', kind=None),
                                    Name(id='feedback_data', ctx=Load()),
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
                            value=Constant(value=' Override of payment to find the transaction based on Ogone data.\n\n        :param str provider: The provider of the acquirer that handled the transaction\n        :param dict data: The feedback data sent by the provider\n        :return: The transaction if found\n        :rtype: recordset of `payment.transaction`\n        :raise: ValidationError if the data match no transaction\n        ', kind=None),
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
                                comparators=[Constant(value='ogone', kind=None)],
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
                                args=[Constant(value='ORDERID', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
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
                                                    Constant(value='ogone', kind=None),
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
                                                left=Constant(value='Ogone: ', kind=None),
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
                            value=Constant(value=' Override of payment to process the transaction based on Ogone data.\n\n        Note: self.ensure_one()\n\n        :param dict data: The feedback data sent by the provider\n        :return: None\n        ', kind=None),
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
                                comparators=[Constant(value='ogone', kind=None)],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='tree', kind=None),
                                ops=[In()],
                                comparators=[Name(id='data', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='data', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='data', ctx=Load()),
                                        slice=Constant(value='tree', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
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
                            value=Call(
                                func=Attribute(
                                    value=Name(id='data', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='PAYID', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='payment_status', ctx=Store())],
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='STATUS', kind=None),
                                            Constant(value='0', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='payment_status', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='const', ctx=Load()),
                                            attr='PAYMENT_STATUS_MAPPING',
                                            ctx=Load(),
                                        ),
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
                                        left=Name(id='payment_status', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='const', ctx=Load()),
                                                    attr='PAYMENT_STATUS_MAPPING',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='done', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='has_token_data', ctx=Store())],
                                            value=Compare(
                                                left=Constant(value='ALIAS', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='data', ctx=Load())],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tokenize',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='has_token_data', ctx=Load()),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_ogone_tokenize_from_feedback_data',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='data', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
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
                                                left=Name(id='payment_status', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='const', ctx=Load()),
                                                            attr='PAYMENT_STATUS_MAPPING',
                                                            ctx=Load(),
                                                        ),
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
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='info',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='received data with invalid payment status: %s', kind=None),
                                                            Name(id='payment_status', ctx=Load()),
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
                                                                left=Constant(value='Ogone: ', kind=None),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='_', ctx=Load()),
                                                                    args=[
                                                                        Constant(value='Received data with invalid payment status: %s', kind=None),
                                                                        Name(id='payment_status', ctx=Load()),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_ogone_tokenize_from_feedback_data',
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
                            value=Constant(value=' Create a token from feedback data.\n\n        :param dict data: The feedback data sent by the provider\n        :return: None\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='token_name', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='CARDNO', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='payment_utils', ctx=Load()),
                                            attr='build_token_name',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='token', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='payment.token', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='acquirer_id', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='acquirer_ref', kind=None),
                                            Constant(value='verified', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='acquirer_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Name(id='token_name', ctx=Load()),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='data', ctx=Load()),
                                                slice=Constant(value='ALIAS', kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value=True, kind=None),
                                        ],
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
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='token_id', kind=None),
                                            Constant(value='tokenize', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='token', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='created token with id %s for partner with id %s', kind=None),
                                    Attribute(
                                        value=Name(id='token', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
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
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
