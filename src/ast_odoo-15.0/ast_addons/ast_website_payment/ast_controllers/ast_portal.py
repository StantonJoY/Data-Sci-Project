Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='http', asname=None),
                alias(name='_', asname=None),
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
        ImportFrom(
            module='odoo.tools.json',
            names=[alias(name='scriptsafe', asname='json_safe')],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.payment',
            names=[alias(name='utils', asname='payment_utils')],
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
                    name='donation_pay',
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
                            value=Constant(value=' Behaves like PaymentPortal.payment_pay but for donation\n\n        :param dict kwargs: As the parameters of in payment_pay, with the additional:\n            - str donation_options: The options settled in the donation snippet\n            - str donation_descriptions: The descriptions for all prefilled amounts\n        :return: The rendered donation form\n        :rtype: str\n        :raise: werkzeug.exceptions.NotFound if the access token is invalid\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='kwargs', ctx=Load()),
                                    slice=Constant(value='is_donation', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='kwargs', ctx=Load()),
                                    slice=Constant(value='currency_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='kwargs', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='currency_id', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='company',
                                                        ctx=Load(),
                                                    ),
                                                    attr='currency_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
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
                            targets=[
                                Subscript(
                                    value=Name(id='kwargs', ctx=Load()),
                                    slice=Constant(value='amount', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='float', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='kwargs', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='amount', kind=None),
                                            Constant(value=25, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='kwargs', ctx=Load()),
                                    slice=Constant(value='donation_options', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='donation_options', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='json_safe', ctx=Load()),
                                            attr='dumps',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='customAmount',
                                                        value=Constant(value='freeAmount', kind=None),
                                                    ),
                                                ],
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
                            test=Call(
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
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='kwargs', ctx=Load()),
                                            slice=Constant(value='partner_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
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
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='kwargs', ctx=Load()),
                                            slice=Constant(value='access_token', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='payment_utils', ctx=Load()),
                                            attr='generate_access_token',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='kwargs', ctx=Load()),
                                                slice=Constant(value='partner_id', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='kwargs', ctx=Load()),
                                                slice=Constant(value='amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='kwargs', ctx=Load()),
                                                slice=Constant(value='currency_id', kind=None),
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='payment_pay',
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
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/donation/pay', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
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
                    name='get_acquirer_fees',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='acquirer_ids', annotation=None, type_comment=None),
                            arg(arg='amount', annotation=None, type_comment=None),
                            arg(arg='currency_id', annotation=None, type_comment=None),
                            arg(arg='country_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
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
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='acquirer_ids', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='currency', ctx=Store())],
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='country', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.country', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='country_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='fees_by_acquirer', ctx=Store())],
                            value=DictComp(
                                key=Attribute(
                                    value=Name(id='acq_sudo', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='acq_sudo', ctx=Load()),
                                        attr='_compute_fees',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Name(id='amount', ctx=Load()),
                                        Name(id='currency', ctx=Load()),
                                        Name(id='country', ctx=Load()),
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
                        Return(
                            value=Name(id='fees_by_acquirer', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/donation/get_acquirer_fees', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
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
                    name='donation_transaction',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='amount', annotation=None, type_comment=None),
                            arg(arg='currency_id', annotation=None, type_comment=None),
                            arg(arg='partner_id', annotation=None, type_comment=None),
                            arg(arg='access_token', annotation=None, type_comment=None),
                            arg(arg='minimum_amount', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[Constant(value=0, kind=None)],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='float', ctx=Load()),
                                    args=[Name(id='amount', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Lt()],
                                comparators=[
                                    Call(
                                        func=Name(id='float', ctx=Load()),
                                        args=[Name(id='minimum_amount', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValidationError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='Donation amount must be at least %.2f.', kind=None),
                                                    Call(
                                                        func=Name(id='float', ctx=Load()),
                                                        args=[Name(id='minimum_amount', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
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
                        Assign(
                            targets=[Name(id='use_public_partner', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
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
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='partner_id', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='use_public_partner', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='details', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='kwargs', ctx=Load()),
                                        slice=Constant(value='partner_details', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='details', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='name', kind=None)],
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
                                                        args=[Constant(value='Name is required.', kind=None)],
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
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='details', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='email', kind=None)],
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
                                                        args=[Constant(value='Email is required.', kind=None)],
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
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='details', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='country_id', kind=None)],
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
                                                        args=[Constant(value='Country is required.', kind=None)],
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
                                Assign(
                                    targets=[Name(id='partner_id', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='website',
                                                    ctx=Load(),
                                                ),
                                                attr='user_id',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Delete(
                                    targets=[
                                        Subscript(
                                            value=Name(id='kwargs', ctx=Load()),
                                            slice=Constant(value='partner_details', kind=None),
                                            ctx=Del(),
                                        ),
                                    ],
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='tx_sudo', ctx=Load()),
                                    attr='is_donation',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='use_public_partner', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tx_sudo', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='partner_name', kind=None),
                                                    Constant(value='partner_email', kind=None),
                                                    Constant(value='partner_country_id', kind=None),
                                                ],
                                                values=[
                                                    Subscript(
                                                        value=Name(id='details', ctx=Load()),
                                                        slice=Constant(value='name', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='details', ctx=Load()),
                                                        slice=Constant(value='email', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='details', ctx=Load()),
                                                        slice=Constant(value='country_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='tx_sudo', ctx=Load()),
                                            attr='partner_country_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='tx_sudo', ctx=Load()),
                                                    attr='partner_country_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='kwargs', ctx=Load()),
                                                    slice=Constant(value='partner_details', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='country_id', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
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
                        Assign(
                            targets=[Name(id='recipient_email', ctx=Store())],
                            value=Subscript(
                                value=Name(id='kwargs', ctx=Load()),
                                slice=Constant(value='donation_recipient_email', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='comment', ctx=Store())],
                            value=Subscript(
                                value=Name(id='kwargs', ctx=Load()),
                                slice=Constant(value='donation_comment', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tx_sudo', ctx=Load()),
                                    attr='_send_donation_email',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=True, kind=None),
                                    Name(id='comment', ctx=Load()),
                                    Name(id='recipient_email', ctx=Load()),
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
                            args=[Constant(value='/donation/transaction/<minimum_amount>', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
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
                    name='_get_custom_rendering_context_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='donation_options', annotation=None, type_comment=None),
                            arg(arg='donation_descriptions', annotation=None, type_comment=None),
                            arg(arg='is_donation', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='rendering_context', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
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
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='is_donation', ctx=Load()),
                            body=[
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
                                    targets=[Name(id='partner_sudo', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='user_sudo', ctx=Load()),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='partner_details', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='countries', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.country', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='logged_in', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='partner_details', ctx=Store())],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='email', kind=None),
                                                    Constant(value='country_id', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='partner_sudo', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='partner_sudo', ctx=Load()),
                                                        attr='email',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='partner_sudo', ctx=Load()),
                                                            attr='country_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='countries', ctx=Store())],
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
                                                        slice=Constant(value='res.country', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='descriptions', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='httprequest',
                                                    ctx=Load(),
                                                ),
                                                attr='form',
                                                ctx=Load(),
                                            ),
                                            attr='getlist',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='donation_descriptions', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='donation_options', ctx=Store())],
                                    value=IfExp(
                                        test=Name(id='donation_options', ctx=Load()),
                                        body=Call(
                                            func=Attribute(
                                                value=Name(id='json_safe', ctx=Load()),
                                                attr='loads',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='donation_options', ctx=Load())],
                                            keywords=[],
                                        ),
                                        orelse=Dict(keys=[], values=[]),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='donation_amounts', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='json_safe', ctx=Load()),
                                            attr='loads',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='donation_options', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='donationAmounts', kind=None),
                                                    Constant(value='[]', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rendering_context', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='is_donation', kind=None),
                                                    Constant(value='partner', kind=None),
                                                    Constant(value='transaction_route', kind=None),
                                                    Constant(value='partner_details', kind=None),
                                                    Constant(value='error', kind=None),
                                                    Constant(value='countries', kind=None),
                                                    Constant(value='donation_options', kind=None),
                                                    Constant(value='donation_amounts', kind=None),
                                                    Constant(value='donation_descriptions', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=True, kind=None),
                                                    Name(id='partner_sudo', ctx=Load()),
                                                    BinOp(
                                                        left=Constant(value='/donation/transaction/%s', kind=None),
                                                        op=Mod(),
                                                        right=Call(
                                                            func=Attribute(
                                                                value=Name(id='donation_options', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Constant(value='minimumAmount', kind=None),
                                                                Constant(value=0, kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    Name(id='partner_details', ctx=Load()),
                                                    Dict(keys=[], values=[]),
                                                    Name(id='countries', ctx=Load()),
                                                    Name(id='donation_options', ctx=Load()),
                                                    Name(id='donation_amounts', ctx=Load()),
                                                    Name(id='descriptions', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='rendering_context', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
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
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='is_donation', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Constant(value='website_payment.donation_pay', kind=None),
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
