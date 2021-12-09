Module(
    body=[
        ImportFrom(
            module='hashlib',
            names=[alias(name='md5', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.float_utils',
            names=[alias(name='float_repr', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='SUPPORTED_CURRENCIES', ctx=Store())],
            value=Tuple(
                elts=[
                    Constant(value='ARS', kind=None),
                    Constant(value='BRL', kind=None),
                    Constant(value='CLP', kind=None),
                    Constant(value='COP', kind=None),
                    Constant(value='MXN', kind=None),
                    Constant(value='PEN', kind=None),
                    Constant(value='USD', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        ClassDef(
            name='PaymentAcquirer',
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
                    value=Constant(value='payment.acquirer', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='provider', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='selection_add',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='payulatam', kind=None),
                                                Constant(value='PayU Latam', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Dict(
                                    keys=[Constant(value='payulatam', kind=None)],
                                    values=[Constant(value='set default', kind=None)],
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='payulatam_merchant_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='PayU Latam Merchant ID', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The ID solely used to identify the account with PayULatam', kind=None),
                            ),
                            keyword(
                                arg='required_if_provider',
                                value=Constant(value='payulatam', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='payulatam_account_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='PayU Latam Account ID', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The ID solely used to identify the country-dependent shop with PayULatam', kind=None),
                            ),
                            keyword(
                                arg='required_if_provider',
                                value=Constant(value='payulatam', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='payulatam_api_key', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='PayU Latam API Key', kind=None),
                            ),
                            keyword(
                                arg='required_if_provider',
                                value=Constant(value='payulatam', kind=None),
                            ),
                            keyword(
                                arg='groups',
                                value=Constant(value='base.group_system', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_compatible_acquirers',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[arg(arg='currency_id', annotation=None, type_comment=None)],
                        kw_defaults=[Constant(value=None, kind=None)],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Override of payment to unlist PayU Latam acquirers for unsupported currencies. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='acquirers', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_compatible_acquirers',
                                    ctx=Load(),
                                ),
                                args=[
                                    Starred(
                                        value=Name(id='args', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='currency_id',
                                        value=Name(id='currency_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='currency', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.currency', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='currency_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='exists',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='currency', ctx=Load()),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='currency', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[Name(id='SUPPORTED_CURRENCIES', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='acquirers', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='acquirers', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='a', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Name(id='a', ctx=Load()),
                                                        attr='provider',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[NotEq()],
                                                    comparators=[Constant(value='payulatam', kind=None)],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='acquirers', ctx=Load()),
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
                    name='_payulatam_generate_sign',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                            arg(arg='incoming', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Generate the signature for incoming or outgoing communications.\n\n        :param dict values: The values used to generate the signature\n        :param bool incoming: Whether the signature must be generated for an incoming (PayU Latam to\n                              Odoo) or outgoing (Odoo to PayU Latam) communication.\n        :return: The signature\n        :rtype: str\n        ', kind=None),
                        ),
                        If(
                            test=Name(id='incoming', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='data_string', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value='~', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='payulatam_api_key',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='payulatam_merchant_id',
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='values', ctx=Load()),
                                                        slice=Constant(value='referenceCode', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Name(id='float_repr', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='float', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='values', ctx=Load()),
                                                                            attr='get',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='TX_VALUE', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Constant(value=1, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Subscript(
                                                        value=Name(id='values', ctx=Load()),
                                                        slice=Constant(value='currency', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='values', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='transactionState', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='data_string', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value='~', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='payulatam_api_key',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='payulatam_merchant_id',
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='values', ctx=Load()),
                                                        slice=Constant(value='referenceCode', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Name(id='float_repr', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='float', ctx=Load()),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='values', ctx=Load()),
                                                                        slice=Constant(value='amount', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Constant(value=1, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Subscript(
                                                        value=Name(id='values', ctx=Load()),
                                                        slice=Constant(value='currency', kind=None),
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
                            ],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='md5', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='data_string', ctx=Load()),
                                                    attr='encode',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='utf-8', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='hexdigest',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_default_payment_method_id',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
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
                                comparators=[Constant(value='payulatam', kind=None)],
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
                                            attr='_get_default_payment_method_id',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='payment_payulatam.payment_method_payulatam', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
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
