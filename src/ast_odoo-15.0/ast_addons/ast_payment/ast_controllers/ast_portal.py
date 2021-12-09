Module(
    body=[
        Import(
            names=[alias(name='urllib.parse', asname=None)],
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
            names=[
                alias(name='UserError', asname=None),
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
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.payment',
            names=[alias(name='utils', asname='payment_utils')],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.payment.controllers.post_processing',
            names=[alias(name='PaymentPostProcessing', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.portal.controllers',
            names=[alias(name='portal', asname=None)],
            level=0,
        ),
        ClassDef(
            name='PaymentPortal',
            bases=[
                Attribute(
                    value=Name(id='portal', ctx=Load()),
                    attr='CustomerPortal',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=" This controller contains the foundations for online payments through the portal.\n\n    It allows to complete a full payment flow without the need of going though a document-based flow\n    made available by another module's controller.\n\n    Such controllers should extend this one to gain access to the _create_transaction static method\n    that implements the creation of a transaction before its processing, or to override specific\n    routes and change their behavior globally (e.g. make the /pay route handle sale orders).\n\n    The following routes are exposed:\n    - `/payment/pay` allows for arbitrary payments.\n    - `/my/payment_method` allows the user to create and delete tokens. It's its own `landing_route`\n    - `/payment/transaction` is the `transaction_route` for the standard payment flow. It creates a\n      draft transaction, and return the processing values necessary for the completion of the\n      transaction.\n    - `/payment/confirmation` is the `landing_route` for the standard payment flow. It displays the\n      payment confirmation page to the user when the transaction is validated.\n    ", kind=None),
                ),
                FunctionDef(
                    name='payment_pay',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='reference', annotation=None, type_comment=None),
                            arg(arg='amount', annotation=None, type_comment=None),
                            arg(arg='currency_id', annotation=None, type_comment=None),
                            arg(arg='partner_id', annotation=None, type_comment=None),
                            arg(arg='company_id', annotation=None, type_comment=None),
                            arg(arg='acquirer_id', annotation=None, type_comment=None),
                            arg(arg='access_token', annotation=None, type_comment=None),
                            arg(arg='invoice_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Display the payment form with optional filtering of payment options.\n\n        The filtering takes place on the basis of provided parameters, if any. If a parameter is\n        incorrect or malformed, it is skipped to avoid preventing the user from making the payment.\n\n        In addition to the desired filtering, a second one ensures that none of the following\n        rules is broken:\n            - Public users are not allowed to save their payment method as a token.\n            - Payments made by public users should either *not* be made on behalf of a specific\n              partner or have an access token validating the partner, amount and currency.\n        We let access rights and security rules do their job for logged in users.\n\n        :param str reference: The custom prefix to compute the full reference\n        :param str amount: The amount to pay\n        :param str currency_id: The desired currency, as a `res.currency` id\n        :param str partner_id: The partner making the payment, as a `res.partner` id\n        :param str company_id: The related company, as a `res.company` id\n        :param str acquirer_id: The desired acquirer, as a `payment.acquirer` id\n        :param str access_token: The access token used to authenticate the partner\n        :param str invoice_id: The account move for which a payment id made, as a `account.move` id\n        :param dict kwargs: Optional data. This parameter is not used here\n        :return: The rendered checkout form\n        :rtype: str\n        :raise: werkzeug.exceptions.NotFound if the access token is invalid\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='currency_id', ctx=Store()),
                                        Name(id='acquirer_id', ctx=Store()),
                                        Name(id='partner_id', ctx=Store()),
                                        Name(id='company_id', ctx=Store()),
                                        Name(id='invoice_id', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='tuple', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='map', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cast_as_int',
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Name(id='currency_id', ctx=Load()),
                                                    Name(id='acquirer_id', ctx=Load()),
                                                    Name(id='partner_id', ctx=Load()),
                                                    Name(id='company_id', ctx=Load()),
                                                    Name(id='invoice_id', ctx=Load()),
                                                ],
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
                        Assign(
                            targets=[Name(id='amount', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='cast_as_float',
                                    ctx=Load(),
                                ),
                                args=[Name(id='amount', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='partner_id', ctx=Load()),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='payment_utils', ctx=Load()),
                                                attr='check_access_token',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='access_token', ctx=Load()),
                                                Name(id='partner_id', ctx=Load()),
                                                Name(id='amount', ctx=Load()),
                                                Name(id='currency_id', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Attribute(
                                                value=Attribute(
                                                    value=Name(id='werkzeug', ctx=Load()),
                                                    attr='exceptions',
                                                    ctx=Load(),
                                                ),
                                                attr='NotFound',
                                                ctx=Load(),
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='user_sudo', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='user',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='logged_in', ctx=Store())],
                            value=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='user_sudo', ctx=Load()),
                                        attr='_is_public',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partner_is_different', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='logged_in', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='partner_is_different', ctx=Store())],
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='partner_id', ctx=Load()),
                                            Compare(
                                                left=Name(id='partner_id', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='user_sudo', ctx=Load()),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='partner_sudo', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='user_sudo', ctx=Load()),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='partner_sudo', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
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
                                                                slice=Constant(value='res.partner', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='partner_id', ctx=Load())],
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
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='partner_sudo', ctx=Load()),
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='redirect',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    JoinedStr(
                                                        values=[
                                                            Constant(value='/web/login?redirect=', kind=None),
                                                            FormattedValue(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='urllib', ctx=Load()),
                                                                            attr='parse',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='quote',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='request', ctx=Load()),
                                                                                attr='httprequest',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='full_path',
                                                                            ctx=Load(),
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
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='reference', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='reference', ctx=Load()),
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
                                                value=Constant(value='tx', kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='amount', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='amount', ctx=Load()),
                                    Constant(value=0.0, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='company_id', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='company_id', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='partner_sudo', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='user_sudo', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='currency_id', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='currency_id', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='res.company', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='company_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='currency_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
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
                                                    value=Name(id='request', ctx=Load()),
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
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='currency', ctx=Load()),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='currency', ctx=Load()),
                                            attr='active',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Attribute(
                                        value=Attribute(
                                            value=Name(id='werkzeug', ctx=Load()),
                                            attr='exceptions',
                                            ctx=Load(),
                                        ),
                                        attr='NotFound',
                                        ctx=Load(),
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='acquirers_sudo', ctx=Store())],
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
                                                slice=Constant(value='payment.acquirer', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_compatible_acquirers',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='company_id', ctx=Load()),
                                    Attribute(
                                        value=Name(id='partner_sudo', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
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
                        If(
                            test=Compare(
                                left=Name(id='acquirer_id', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='acquirers_sudo', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='acquirers_sudo', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='acquirers_sudo', ctx=Load()),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='acquirer_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='payment_tokens', ctx=Store())],
                            value=IfExp(
                                test=Name(id='logged_in', ctx=Load()),
                                body=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='payment.token', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='search',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='acquirer_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Attribute(
                                                            value=Name(id='acquirers_sudo', ctx=Load()),
                                                            attr='ids',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                Tuple(
                                                    elts=[
                                                        Constant(value='partner_id', kind=None),
                                                        Constant(value='=', kind=None),
                                                        Attribute(
                                                            value=Name(id='partner_sudo', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                orelse=Subscript(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='payment.token', kind=None),
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='fees_by_acquirer', ctx=Store())],
                            value=DictComp(
                                key=Name(id='acq_sudo', ctx=Load()),
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='acq_sudo', ctx=Load()),
                                        attr='_compute_fees',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Name(id='amount', ctx=Load()),
                                        Name(id='currency', ctx=Load()),
                                        Attribute(
                                            value=Name(id='partner_sudo', ctx=Load()),
                                            attr='country_id',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='acq_sudo', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='acquirers_sudo', ctx=Load()),
                                                attr='filtered',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='fees_active', kind=None)],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='access_token', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='payment_utils', ctx=Load()),
                                    attr='generate_access_token',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='partner_sudo', ctx=Load()),
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rendering_context', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='acquirers', kind=None),
                                    Constant(value='tokens', kind=None),
                                    Constant(value='fees_by_acquirer', kind=None),
                                    Constant(value='show_tokenize_input', kind=None),
                                    Constant(value='reference_prefix', kind=None),
                                    Constant(value='amount', kind=None),
                                    Constant(value='currency', kind=None),
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='access_token', kind=None),
                                    Constant(value='transaction_route', kind=None),
                                    Constant(value='landing_route', kind=None),
                                    Constant(value='partner_is_different', kind=None),
                                    Constant(value='invoice_id', kind=None),
                                    None,
                                ],
                                values=[
                                    Name(id='acquirers_sudo', ctx=Load()),
                                    Name(id='payment_tokens', ctx=Load()),
                                    Name(id='fees_by_acquirer', ctx=Load()),
                                    Name(id='logged_in', ctx=Load()),
                                    Name(id='reference', ctx=Load()),
                                    Name(id='amount', ctx=Load()),
                                    Name(id='currency', ctx=Load()),
                                    Attribute(
                                        value=Name(id='partner_sudo', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='access_token', ctx=Load()),
                                    Constant(value='/payment/transaction', kind=None),
                                    Constant(value='/payment/confirmation', kind=None),
                                    Name(id='partner_is_different', ctx=Load()),
                                    Name(id='invoice_id', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_custom_rendering_context_values',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg=None,
                                                value=Name(id='kwargs', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_payment_page_template_xmlid',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg=None,
                                                value=Name(id='kwargs', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Name(id='rendering_context', ctx=Load()),
                                ],
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
                            args=[Constant(value='/payment/pay', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='GET', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                                keyword(
                                    arg='sitemap',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_payment_page_template_xmlid',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Constant(value='payment.pay', kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='payment_method',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Display the form to manage payment methods.\n\n        :param dict kwargs: Optional data. This parameter is not used here\n        :return: The rendered manage form\n        :rtype: str\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='partner', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='user',
                                    ctx=Load(),
                                ),
                                attr='partner_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='acquirers_sudo', ctx=Store())],
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
                                                slice=Constant(value='payment.acquirer', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_compatible_acquirers',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='company',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='force_tokenization',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='is_validation',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tokens', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='payment_token_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='union',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='commercial_partner_id',
                                                    ctx=Load(),
                                                ),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='payment_token_ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='access_token', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='payment_utils', ctx=Load()),
                                    attr='generate_access_token',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value=None, kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rendering_context', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='acquirers', kind=None),
                                    Constant(value='tokens', kind=None),
                                    Constant(value='reference_prefix', kind=None),
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='access_token', kind=None),
                                    Constant(value='transaction_route', kind=None),
                                    Constant(value='landing_route', kind=None),
                                    None,
                                ],
                                values=[
                                    Name(id='acquirers_sudo', ctx=Load()),
                                    Name(id='tokens', ctx=Load()),
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
                                                value=Constant(value='validation', kind=None),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='access_token', ctx=Load()),
                                    Constant(value='/payment/transaction', kind=None),
                                    Constant(value='/my/payment_method', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_custom_rendering_context_values',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg=None,
                                                value=Name(id='kwargs', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='payment.payment_methods', kind=None),
                                    Name(id='rendering_context', ctx=Load()),
                                ],
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
                            args=[Constant(value='/my/payment_method', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='GET', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_custom_rendering_context_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return a dict of additional rendering context values.\n\n        :param dict kwargs: Optional data. This parameter is not used here\n        :return: The dict of additional rendering context values\n        :rtype: dict\n        ', kind=None),
                        ),
                        Return(
                            value=Dict(keys=[], values=[]),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='payment_transaction',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='amount', annotation=None, type_comment=None),
                            arg(arg='currency_id', annotation=None, type_comment=None),
                            arg(arg='partner_id', annotation=None, type_comment=None),
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
                            value=Constant(value=' Create a draft transaction and return its processing values.\n\n        :param float|None amount: The amount to pay in the given currency.\n                                  None if in a payment method validation operation\n        :param int|None currency_id: The currency of the transaction, as a `res.currency` id.\n                                     None if in a payment method validation operation\n        :param int partner_id: The partner making the payment, as a `res.partner` id\n        :param str access_token: The access token used to authenticate the partner\n        :param dict kwargs: Locally unused data passed to `_create_transaction`\n        :return: The mandatory values for the processing of the transaction\n        :rtype: dict\n        :raise: ValidationError if the access token is invalid\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='amount', ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='amount', ctx=Load()),
                                    Call(
                                        func=Name(id='float', ctx=Load()),
                                        args=[Name(id='amount', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='payment_utils', ctx=Load()),
                                        attr='check_access_token',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Name(id='access_token', ctx=Load()),
                                        Name(id='partner_id', ctx=Load()),
                                        Name(id='amount', ctx=Load()),
                                        Name(id='currency_id', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValidationError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='The access token is invalid.', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
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
                                        arg='amount',
                                        value=Name(id='amount', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='currency_id',
                                        value=Name(id='currency_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='partner_id',
                                        value=Name(id='partner_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_update_landing_route',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='tx_sudo', ctx=Load()),
                                    Name(id='access_token', ctx=Load()),
                                ],
                                keywords=[],
                            ),
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
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/payment/transaction', kind=None)],
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
                FunctionDef(
                    name='_create_transaction',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='payment_option_id', annotation=None, type_comment=None),
                            arg(arg='reference_prefix', annotation=None, type_comment=None),
                            arg(arg='amount', annotation=None, type_comment=None),
                            arg(arg='currency_id', annotation=None, type_comment=None),
                            arg(arg='partner_id', annotation=None, type_comment=None),
                            arg(arg='flow', annotation=None, type_comment=None),
                            arg(arg='tokenization_requested', annotation=None, type_comment=None),
                            arg(arg='landing_route', annotation=None, type_comment=None),
                            arg(arg='is_validation', annotation=None, type_comment=None),
                            arg(arg='invoice_id', annotation=None, type_comment=None),
                            arg(arg='custom_create_values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Create a draft transaction based on the payment context and return it.\n\n        :param int payment_option_id: The payment option handling the transaction, as a\n                                      `payment.acquirer` id or a `payment.token` id\n        :param str reference_prefix: The custom prefix to compute the full reference\n        :param float|None amount: The amount to pay in the given currency.\n                                  None if in a payment method validation operation\n        :param int|None currency_id: The currency of the transaction, as a `res.currency` id.\n                                     None if in a payment method validation operation\n        :param int partner_id: The partner making the payment, as a `res.partner` id\n        :param str flow: The online payment flow of the transaction: 'redirect', 'direct' or 'token'\n        :param bool tokenization_requested: Whether the user requested that a token is created\n        :param str landing_route: The route the user is redirected to after the transaction\n        :param bool is_validation: Whether the operation is a validation\n        :param int invoice_id: The account move for which a payment id made, as an `account.move` id\n        :param dict custom_create_values: Additional create values overwriting the default ones\n        :param dict kwargs: Locally unused data passed to `_is_tokenization_required` and\n                            `_compute_reference`\n        :return: The sudoed transaction that was created\n        :rtype: recordset of `payment.transaction`\n        :raise: UserError if the flow is invalid\n        ", kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='flow', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    List(
                                        elts=[
                                            Constant(value='redirect', kind=None),
                                            Constant(value='direct', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='acquirer_sudo', ctx=Store())],
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
                                                        slice=Constant(value='payment.acquirer', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='payment_option_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='token_id', ctx=Store())],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='tokenization_required_or_requested', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='acquirer_sudo', ctx=Load()),
                                                    attr='_is_tokenization_required',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='provider',
                                                        value=Attribute(
                                                            value=Name(id='acquirer_sudo', ctx=Load()),
                                                            attr='provider',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg=None,
                                                        value=Name(id='kwargs', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            Name(id='tokenization_requested', ctx=Load()),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='tokenize', ctx=Store())],
                                    value=Call(
                                        func=Name(id='bool', ctx=Load()),
                                        args=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='request', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='user',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='_is_public',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='acquirer_sudo', ctx=Load()),
                                                        attr='allow_tokenization',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='tokenization_required_or_requested', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='flow', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='token', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='token_sudo', ctx=Store())],
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
                                                                slice=Constant(value='payment.token', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='payment_option_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='acquirer_sudo', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='token_sudo', ctx=Load()),
                                                attr='acquirer_id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='token_id', ctx=Store())],
                                            value=Name(id='payment_option_id', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='tokenize', ctx=Store())],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='The payment should either be direct, with redirection, or made by a token.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        If(
                            test=Name(id='invoice_id', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='custom_create_values', ctx=Load()),
                                        ops=[Is()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='custom_create_values', ctx=Store())],
                                            value=Dict(keys=[], values=[]),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='custom_create_values', ctx=Load()),
                                            slice=Constant(value='invoice_ids', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
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
                                                            Call(
                                                                func=Name(id='int', ctx=Load()),
                                                                args=[Name(id='invoice_id', ctx=Load())],
                                                                keywords=[],
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
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='reference', ctx=Store())],
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
                                    attr='_compute_reference',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='acquirer_sudo', ctx=Load()),
                                        attr='provider',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='prefix',
                                        value=Name(id='reference_prefix', ctx=Load()),
                                    ),
                                    keyword(
                                        arg=None,
                                        value=BoolOp(
                                            op=Or(),
                                            values=[
                                                Name(id='custom_create_values', ctx=Load()),
                                                Dict(keys=[], values=[]),
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
                        If(
                            test=Name(id='is_validation', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='amount', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='acquirer_sudo', ctx=Load()),
                                            attr='_get_validation_amount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='currency_id', ctx=Store())],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='acquirer_sudo', ctx=Load()),
                                                attr='_get_validation_currency',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='tx_sudo', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='acquirer_id', kind=None),
                                            Constant(value='reference', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='token_id', kind=None),
                                            Constant(value='operation', kind=None),
                                            Constant(value='tokenize', kind=None),
                                            Constant(value='landing_route', kind=None),
                                            None,
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='acquirer_sudo', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Name(id='reference', ctx=Load()),
                                            Name(id='amount', ctx=Load()),
                                            Name(id='currency_id', ctx=Load()),
                                            Name(id='partner_id', ctx=Load()),
                                            Name(id='token_id', ctx=Load()),
                                            IfExp(
                                                test=UnaryOp(
                                                    op=Not(),
                                                    operand=Name(id='is_validation', ctx=Load()),
                                                ),
                                                body=JoinedStr(
                                                    values=[
                                                        Constant(value='online_', kind=None),
                                                        FormattedValue(
                                                            value=Name(id='flow', ctx=Load()),
                                                            conversion=-1,
                                                            format_spec=None,
                                                        ),
                                                    ],
                                                ),
                                                orelse=Constant(value='validation', kind=None),
                                            ),
                                            Name(id='tokenize', ctx=Load()),
                                            Name(id='landing_route', ctx=Load()),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='custom_create_values', ctx=Load()),
                                                    Dict(keys=[], values=[]),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='flow', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='token', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tx_sudo', ctx=Load()),
                                            attr='_send_payment_request',
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
                                            value=Name(id='tx_sudo', ctx=Load()),
                                            attr='_log_sent_message',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='PaymentPostProcessing', ctx=Load()),
                                    attr='monitor_transactions',
                                    ctx=Load(),
                                ),
                                args=[Name(id='tx_sudo', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='tx_sudo', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_update_landing_route',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='tx_sudo', annotation=None, type_comment=None),
                            arg(arg='access_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Add the mandatory parameters to the route and recompute the access token if needed.\n\n        The generic landing route requires the tx id and access token to be provided since there is\n        no document to rely on. The access token is recomputed in case we are dealing with a\n        validation transaction (acquirer-specific amount and currency).\n\n        :param recordset tx_sudo: The transaction whose landing routes to update, as a\n                                  `payment.transaction` record.\n        :param str access_token: The access token used to authenticate the partner\n        :return: None\n        ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='tx_sudo', ctx=Load()),
                                    attr='operation',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='validation', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='access_token', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='payment_utils', ctx=Load()),
                                            attr='generate_access_token',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='tx_sudo', ctx=Load()),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='tx_sudo', ctx=Load()),
                                                attr='amount',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='tx_sudo', ctx=Load()),
                                                    attr='currency_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
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
                                Attribute(
                                    value=Name(id='tx_sudo', ctx=Load()),
                                    attr='landing_route',
                                    ctx=Store(),
                                ),
                            ],
                            value=JoinedStr(
                                values=[
                                    FormattedValue(
                                        value=Attribute(
                                            value=Name(id='tx_sudo', ctx=Load()),
                                            attr='landing_route',
                                            ctx=Load(),
                                        ),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                    Constant(value='?tx_id=', kind=None),
                                    FormattedValue(
                                        value=Attribute(
                                            value=Name(id='tx_sudo', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                    Constant(value='&access_token=', kind=None),
                                    FormattedValue(
                                        value=Name(id='access_token', ctx=Load()),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='staticmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='payment_confirm',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='tx_id', annotation=None, type_comment=None),
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
                            value=Constant(value=' Display the payment confirmation page with the appropriate status message to the user.\n\n        :param str tx_id: The transaction to confirm, as a `payment.transaction` id\n        :param str access_token: The access token used to verify the user\n        :param dict kwargs: Optional data. This parameter is not used here\n        :raise: werkzeug.exceptions.NotFound if the access token is invalid\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='tx_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='cast_as_int',
                                    ctx=Load(),
                                ),
                                args=[Name(id='tx_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='tx_id', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='tx_sudo', ctx=Store())],
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
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='tx_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='payment_utils', ctx=Load()),
                                                attr='check_access_token',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='access_token', ctx=Load()),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='tx_sudo', ctx=Load()),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='tx_sudo', ctx=Load()),
                                                    attr='amount',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='tx_sudo', ctx=Load()),
                                                        attr='currency_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Attribute(
                                                value=Attribute(
                                                    value=Name(id='werkzeug', ctx=Load()),
                                                    attr='exceptions',
                                                    ctx=Load(),
                                                ),
                                                attr='NotFound',
                                                ctx=Load(),
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='tx_sudo', ctx=Load()),
                                            attr='state',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='draft', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='status', ctx=Store())],
                                            value=Constant(value='info', kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='message', ctx=Store())],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='tx_sudo', ctx=Load()),
                                                        attr='state_message',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='This payment has not been processed yet.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='tx_sudo', ctx=Load()),
                                                    attr='state',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='pending', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='status', ctx=Store())],
                                                    value=Constant(value='warning', kind=None),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='message', ctx=Store())],
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='tx_sudo', ctx=Load()),
                                                            attr='acquirer_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='pending_msg',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='tx_sudo', ctx=Load()),
                                                            attr='state',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[In()],
                                                        comparators=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='authorized', kind=None),
                                                                    Constant(value='done', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='status', ctx=Store())],
                                                            value=Constant(value='success', kind=None),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='message', ctx=Store())],
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='tx_sudo', ctx=Load()),
                                                                    attr='acquirer_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='done_msg',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='tx_sudo', ctx=Load()),
                                                                    attr='state',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='cancel', kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='status', ctx=Store())],
                                                                    value=Constant(value='danger', kind=None),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='message', ctx=Store())],
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='tx_sudo', ctx=Load()),
                                                                            attr='acquirer_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='cancel_msg',
                                                                        ctx=Load(),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Assign(
                                                                    targets=[Name(id='status', ctx=Store())],
                                                                    value=Constant(value='danger', kind=None),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='message', ctx=Store())],
                                                                    value=BoolOp(
                                                                        op=Or(),
                                                                        values=[
                                                                            Attribute(
                                                                                value=Name(id='tx_sudo', ctx=Load()),
                                                                                attr='state_message',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Call(
                                                                                func=Name(id='_', ctx=Load()),
                                                                                args=[Constant(value='An error occurred during the processing of this payment.', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='PaymentPostProcessing', ctx=Load()),
                                            attr='remove_transactions',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='tx_sudo', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='render_values', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='tx', kind=None),
                                            Constant(value='status', kind=None),
                                            Constant(value='message', kind=None),
                                        ],
                                        values=[
                                            Name(id='tx_sudo', ctx=Load()),
                                            Name(id='status', ctx=Load()),
                                            Name(id='message', ctx=Load()),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='render',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='payment.confirm', kind=None),
                                            Name(id='render_values', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='redirect',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='/my/home', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/payment/confirmation', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='GET', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='cast_as_int',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='str_value', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Cast a string as an `int` and return it.\n\n        If the conversion fails, `None` is returned instead.\n\n        :param str str_value: The value to cast as an `int`\n        :return: The casted value, possibly replaced by None if incompatible\n        :rtype: int|None\n        ', kind=None),
                        ),
                        Try(
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[Name(id='str_value', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Tuple(
                                        elts=[
                                            Name(id='TypeError', ctx=Load()),
                                            Name(id='ValueError', ctx=Load()),
                                            Name(id='OverflowError', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[
                                        Return(
                                            value=Constant(value=None, kind=None),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[Name(id='staticmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='cast_as_float',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='str_value', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Cast a string as a `float` and return it.\n\n        If the conversion fails, `None` is returned instead.\n\n        :param str str_value: The value to cast as a `float`\n        :return: The casted value, possibly replaced by None if incompatible\n        :rtype: float|None\n        ', kind=None),
                        ),
                        Try(
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='float', ctx=Load()),
                                        args=[Name(id='str_value', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Tuple(
                                        elts=[
                                            Name(id='TypeError', ctx=Load()),
                                            Name(id='ValueError', ctx=Load()),
                                            Name(id='OverflowError', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[
                                        Return(
                                            value=Constant(value=None, kind=None),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[Name(id='staticmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
