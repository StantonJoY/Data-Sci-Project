Module(
    body=[
        ImportFrom(
            module='odoo.exceptions',
            names=[
                alias(name='AccessError', asname=None),
                alias(name='MissingError', asname=None),
                alias(name='ValidationError', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.fields',
            names=[alias(name='Command', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='route', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.payment.controllers',
            names=[alias(name='portal', asname='payment_portal')],
            level=0,
        ),
        ClassDef(
            name='PaymentPortal',
            bases=[
                Attribute(
                    value=Name(id='payment_portal', ctx=Load()),
                    attr='PaymentPortal',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='invoice_transaction',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='invoice_id', annotation=None, type_comment=None),
                            arg(arg='access_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Create a draft transaction and return its processing values.\n\n        :param int invoice_id: The invoice to pay, as an `account.move` id\n        :param str access_token: The access token used to authenticate the request\n        :param dict kwargs: Locally unused data passed to `_create_transaction`\n        :return: The mandatory values for the processing of the transaction\n        :rtype: dict\n        :raise: ValidationError if the invoice id or the access token is invalid\n        ', kind=None),
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_document_check_access',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='account.move', kind=None),
                                            Name(id='invoice_id', ctx=Load()),
                                            Name(id='access_token', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='MissingError', ctx=Load()),
                                    name='error',
                                    body=[
                                        Raise(
                                            exc=Name(id='error', ctx=Load()),
                                            cause=None,
                                        ),
                                    ],
                                ),
                                ExceptHandler(
                                    type=Name(id='AccessError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValidationError', ctx=Load()),
                                                args=[Constant(value='The access token is invalid.', kind=None)],
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
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='kwargs', ctx=Load()),
                                    slice=Constant(value='reference_prefix', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='custom_create_values', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tx_sudo', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_create_transaction',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='custom_create_values',
                                        value=Dict(
                                            keys=[Constant(value='invoice_ids', kind=None)],
                                            values=[
                                                List(
                                                    elts=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='Command', ctx=Load()),
                                                                attr='set',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                List(
                                                                    elts=[Name(id='invoice_id', ctx=Load())],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tx_sudo', ctx=Load()),
                                    attr='_get_processing_values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='route', ctx=Load()),
                            args=[Constant(value='/invoice/transaction/<int:invoice_id>', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
