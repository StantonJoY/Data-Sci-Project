Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='pprint', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='http', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='ValidationError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
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
            name='OgoneController',
            bases=[
                Attribute(
                    value=Name(id='http', ctx=Load()),
                    attr='Controller',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_return_url', ctx=Store())],
                    value=Constant(value='/payment/ogone/return', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_backward_compatibility_urls', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='/payment/ogone/accept', kind=None),
                            Constant(value='/payment/ogone/test/accept', kind=None),
                            Constant(value='/payment/ogone/decline', kind=None),
                            Constant(value='/payment/ogone/test/decline', kind=None),
                            Constant(value='/payment/ogone/exception', kind=None),
                            Constant(value='/payment/ogone/test/exception', kind=None),
                            Constant(value='/payment/ogone/cancel', kind=None),
                            Constant(value='/payment/ogone/test/cancel', kind=None),
                            Constant(value='/payment/ogone/validate/accept', kind=None),
                            Constant(value='/payment/ogone/validate/decline', kind=None),
                            Constant(value='/payment/ogone/validate/exception', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='ogone_return_from_redirect',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='feedback_data', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Process the data returned by Ogone after redirection to the Hosted Payment Page.\n\n        This route can also accept S2S notifications from Ogone if it is configured as a webhook in\n        Ogone's backend.\n\n        :param dict feedback_data: The feedback data\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_homogenize_data',
                                    ctx=Load(),
                                ),
                                args=[Name(id='feedback_data', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_verify_signature',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='feedback_data', ctx=Load()),
                                    Name(id='data', ctx=Load()),
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
                                    Constant(value='entering _handle_feedback_data with data:\n%s', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='pprint', ctx=Load()),
                                            attr='pformat',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='data', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='payment.transaction', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_handle_feedback_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='ogone', kind=None),
                                    Name(id='data', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='redirect',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/payment/status', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[
                                BinOp(
                                    left=List(
                                        elts=[Name(id='_return_url', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Name(id='_backward_compatibility_urls', ctx=Load()),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[
                                            Constant(value='GET', kind=None),
                                            Constant(value='POST', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                                keyword(
                                    arg='csrf',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_homogenize_data',
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
                            value=Constant(value=" Format keys to follow an homogenized convention inspired by Ogone Directlink API.\n\n        The keys received from Ogone APIs have inconsistent formatting and must be homogenized to\n        allow re-using the same methods. We reformat them to follow a unified nomenclature inspired\n        by DirectLink's order direct endpoint.\n\n        Formatting steps:\n        1) Uppercase key strings: 'Something' -> 'SOMETHING', 'something' -> 'SOMETHING'\n        2) Remove the prefix: 'CARD.SOMETHING' -> 'SOMETHING', 'ALIAS.SOMETHING' -> 'SOMETHING'\n        ", kind=None),
                        ),
                        Return(
                            value=DictComp(
                                key=Call(
                                    func=Attribute(
                                        value=Name(id='re', ctx=Load()),
                                        attr='sub',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='.*\\.', kind=None),
                                        Constant(value='', kind=None),
                                        Call(
                                            func=Attribute(
                                                value=Name(id='k', ctx=Load()),
                                                attr='upper',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
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
                FunctionDef(
                    name='_verify_signature',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='sign_data', annotation=None, type_comment=None),
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
                            value=Constant(value=" Check that the signature computed from the feedback matches the received one.\n\n        :param dict sign_data: The original feedback data used to compute the signature\n        :param dict sign_data: The formatted feedback data used to find the tx and received sig\n        :return: None\n        :raise: ValidationError if the signatures don't match\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='acquirer_sudo', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='payment.transaction', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='_get_tx_from_feedback_data',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='ogone', kind=None),
                                        Name(id='data', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                attr='acquirer_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='received_signature', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='data', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='SHASIGN', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_signature', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='acquirer_sudo', ctx=Load()),
                                    attr='_ogone_generate_signature',
                                    ctx=Load(),
                                ),
                                args=[Name(id='sign_data', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='received_signature', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='expected_signature', ctx=Load()),
                                            attr='upper',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
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
                                                    args=[Constant(value='Received data with invalid signature. expected: %(exp)s ; received: %(rec)s ; data:\n%(data)s', kind=None)],
                                                    keywords=[
                                                        keyword(
                                                            arg='exp',
                                                            value=Name(id='expected_signature', ctx=Load()),
                                                        ),
                                                        keyword(
                                                            arg='rec',
                                                            value=Name(id='received_signature', ctx=Load()),
                                                        ),
                                                        keyword(
                                                            arg='data',
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='pprint', ctx=Load()),
                                                                    attr='pformat',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='sign_data', ctx=Load())],
                                                                keywords=[],
                                                            ),
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
