Module(
    body=[
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.image',
            names=[alias(name='image_data_uri', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='werkzeug', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug.exceptions', asname=None)],
        ),
        ClassDef(
            name='ResPartnerBank',
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
                    value=Constant(value='res.partner.bank', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_build_qr_code_vals',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='amount', annotation=None, type_comment=None),
                            arg(arg='free_communication', annotation=None, type_comment=None),
                            arg(arg='structured_communication', annotation=None, type_comment=None),
                            arg(arg='currency', annotation=None, type_comment=None),
                            arg(arg='debtor_partner', annotation=None, type_comment=None),
                            arg(arg='qr_method', annotation=None, type_comment=None),
                            arg(arg='silent_errors', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Returns the QR-code vals needed to generate the QR-code report link to pay this account with the given parameters,\n        or None if no QR-code could be generated.\n\n        :param amount: The amount to be paid\n        :param free_communication: Free communication to add to the payment when generating one with the QR-code\n        :param structured_communication: Structured communication to add to the payment when generating one with the QR-code\n        :param currency: The currency in which amount is expressed\n        :param debtor_partner: The partner to which this QR-code is aimed (so the one who will have to pay)\n        :param qr_method: The QR generation method to be used to make the QR-code. If None, the first one giving a result will be used.\n        :param silent_errors: If true, forbids errors to be raised if some tested QR-code format can't be generated because of incorrect data.\n        ", kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='self', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=None, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
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
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='currency', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Currency must always be provided in order to generate a QR-code', kind=None)],
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
                            targets=[Name(id='available_qr_methods', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_available_qr_methods_in_sequence',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='candidate_methods', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='qr_method', ctx=Load()),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id='qr_method', ctx=Load()),
                                                            Subscript(
                                                                value=Call(
                                                                    func=Name(id='dict', ctx=Load()),
                                                                    args=[Name(id='available_qr_methods', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                slice=Name(id='qr_method', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Name(id='available_qr_methods', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='candidate_method', ctx=Store()),
                                    Name(id='candidate_name', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='candidate_methods', ctx=Load()),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_eligible_for_qr_code',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='candidate_method', ctx=Load()),
                                            Name(id='debtor_partner', ctx=Load()),
                                            Name(id='currency', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='error_message', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_check_for_qr_code_errors',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='candidate_method', ctx=Load()),
                                                    Name(id='amount', ctx=Load()),
                                                    Name(id='currency', ctx=Load()),
                                                    Name(id='debtor_partner', ctx=Load()),
                                                    Name(id='free_communication', ctx=Load()),
                                                    Name(id='structured_communication', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='error_message', ctx=Load()),
                                            ),
                                            body=[
                                                Return(
                                                    value=Dict(
                                                        keys=[
                                                            Constant(value='qr_method', kind=None),
                                                            Constant(value='amount', kind=None),
                                                            Constant(value='currency', kind=None),
                                                            Constant(value='debtor_partner', kind=None),
                                                            Constant(value='free_communication', kind=None),
                                                            Constant(value='structured_communication', kind=None),
                                                        ],
                                                        values=[
                                                            Name(id='candidate_method', ctx=Load()),
                                                            Name(id='amount', ctx=Load()),
                                                            Name(id='currency', ctx=Load()),
                                                            Name(id='debtor_partner', ctx=Load()),
                                                            Name(id='free_communication', ctx=Load()),
                                                            Name(id='structured_communication', ctx=Load()),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='silent_errors', ctx=Load()),
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='error_header', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[
                                                                    Constant(value="The following error prevented '%s' QR-code to be generated though it was detected as eligible: ", kind=None),
                                                                    Name(id='candidate_name', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Raise(
                                                            exc=Call(
                                                                func=Name(id='UserError', ctx=Load()),
                                                                args=[
                                                                    BinOp(
                                                                        left=Name(id='error_header', ctx=Load()),
                                                                        op=Add(),
                                                                        right=Name(id='error_message', ctx=Load()),
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
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Constant(value=None, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='build_qr_code_url',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='amount', annotation=None, type_comment=None),
                            arg(arg='free_communication', annotation=None, type_comment=None),
                            arg(arg='structured_communication', annotation=None, type_comment=None),
                            arg(arg='currency', annotation=None, type_comment=None),
                            arg(arg='debtor_partner', annotation=None, type_comment=None),
                            arg(arg='qr_method', annotation=None, type_comment=None),
                            arg(arg='silent_errors', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='vals', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_build_qr_code_vals',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='amount', ctx=Load()),
                                    Name(id='free_communication', ctx=Load()),
                                    Name(id='structured_communication', ctx=Load()),
                                    Name(id='currency', ctx=Load()),
                                    Name(id='debtor_partner', ctx=Load()),
                                    Name(id='qr_method', ctx=Load()),
                                    Name(id='silent_errors', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='vals', ctx=Load()),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_qr_code_url',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='vals', ctx=Load()),
                                                slice=Constant(value='qr_method', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='vals', ctx=Load()),
                                                slice=Constant(value='amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='vals', ctx=Load()),
                                                slice=Constant(value='currency', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='vals', ctx=Load()),
                                                slice=Constant(value='debtor_partner', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='vals', ctx=Load()),
                                                slice=Constant(value='free_communication', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='vals', ctx=Load()),
                                                slice=Constant(value='structured_communication', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=None, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='build_qr_code_base64',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='amount', annotation=None, type_comment=None),
                            arg(arg='free_communication', annotation=None, type_comment=None),
                            arg(arg='structured_communication', annotation=None, type_comment=None),
                            arg(arg='currency', annotation=None, type_comment=None),
                            arg(arg='debtor_partner', annotation=None, type_comment=None),
                            arg(arg='qr_method', annotation=None, type_comment=None),
                            arg(arg='silent_errors', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='vals', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_build_qr_code_vals',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='amount', ctx=Load()),
                                    Name(id='free_communication', ctx=Load()),
                                    Name(id='structured_communication', ctx=Load()),
                                    Name(id='currency', ctx=Load()),
                                    Name(id='debtor_partner', ctx=Load()),
                                    Name(id='qr_method', ctx=Load()),
                                    Name(id='silent_errors', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='vals', ctx=Load()),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_qr_code_base64',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='vals', ctx=Load()),
                                                slice=Constant(value='qr_method', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='vals', ctx=Load()),
                                                slice=Constant(value='amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='vals', ctx=Load()),
                                                slice=Constant(value='currency', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='vals', ctx=Load()),
                                                slice=Constant(value='debtor_partner', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='vals', ctx=Load()),
                                                slice=Constant(value='free_communication', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='vals', ctx=Load()),
                                                slice=Constant(value='structured_communication', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=None, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_qr_vals',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='qr_method', annotation=None, type_comment=None),
                            arg(arg='amount', annotation=None, type_comment=None),
                            arg(arg='currency', annotation=None, type_comment=None),
                            arg(arg='debtor_partner', annotation=None, type_comment=None),
                            arg(arg='free_communication', annotation=None, type_comment=None),
                            arg(arg='structured_communication', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Constant(value=None, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_qr_code_generation_params',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='qr_method', annotation=None, type_comment=None),
                            arg(arg='amount', annotation=None, type_comment=None),
                            arg(arg='currency', annotation=None, type_comment=None),
                            arg(arg='debtor_partner', annotation=None, type_comment=None),
                            arg(arg='free_communication', annotation=None, type_comment=None),
                            arg(arg='structured_communication', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Constant(value=None, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_qr_code_url',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='qr_method', annotation=None, type_comment=None),
                            arg(arg='amount', annotation=None, type_comment=None),
                            arg(arg='currency', annotation=None, type_comment=None),
                            arg(arg='debtor_partner', annotation=None, type_comment=None),
                            arg(arg='free_communication', annotation=None, type_comment=None),
                            arg(arg='structured_communication', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Hook for extension, to support the different QR generation methods.\n        This function uses the provided qr_method to try generation a QR-code for\n        the given data. It it succeeds, it returns the report URL to make this\n        QR-code; else None.\n\n        :param qr_method: The QR generation method to be used to make the QR-code.\n        :param amount: The amount to be paid\n        :param currency: The currency in which amount is expressed\n        :param debtor_partner: The partner to which this QR-code is aimed (so the one who will have to pay)\n        :param free_communication: Free communication to add to the payment when generating one with the QR-code\n        :param structured_communication: Structured communication to add to the payment when generating one with the QR-code\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='params', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_qr_code_generation_params',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='qr_method', ctx=Load()),
                                    Name(id='amount', ctx=Load()),
                                    Name(id='currency', ctx=Load()),
                                    Name(id='debtor_partner', ctx=Load()),
                                    Name(id='free_communication', ctx=Load()),
                                    Name(id='structured_communication', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='params', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='params', ctx=Load()),
                                            slice=Constant(value='type', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='params', ctx=Load()),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='barcode_type', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=BinOp(
                                        left=Constant(value='/report/barcode/?', kind=None),
                                        op=Add(),
                                        right=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='werkzeug', ctx=Load()),
                                                    attr='urls',
                                                    ctx=Load(),
                                                ),
                                                attr='url_encode',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='params', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=None, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_qr_code_base64',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='qr_method', annotation=None, type_comment=None),
                            arg(arg='amount', annotation=None, type_comment=None),
                            arg(arg='currency', annotation=None, type_comment=None),
                            arg(arg='debtor_partner', annotation=None, type_comment=None),
                            arg(arg='free_communication', annotation=None, type_comment=None),
                            arg(arg='structured_communication', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Hook for extension, to support the different QR generation methods.\n        This function uses the provided qr_method to try generation a QR-code for\n        the given data. It it succeeds, it returns QR code in base64 url; else None.\n\n        :param qr_method: The QR generation method to be used to make the QR-code.\n        :param amount: The amount to be paid\n        :param currency: The currency in which amount is expressed\n        :param debtor_partner: The partner to which this QR-code is aimed (so the one who will have to pay)\n        :param free_communication: Free communication to add to the payment when generating one with the QR-code\n        :param structured_communication: Structured communication to add to the payment when generating one with the QR-code\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='params', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_qr_code_generation_params',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='qr_method', ctx=Load()),
                                    Name(id='amount', ctx=Load()),
                                    Name(id='currency', ctx=Load()),
                                    Name(id='debtor_partner', ctx=Load()),
                                    Name(id='free_communication', ctx=Load()),
                                    Name(id='structured_communication', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='params', ctx=Load()),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='barcode', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='ir.actions.report', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='barcode',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg=None,
                                                        value=Name(id='params', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Tuple(
                                                elts=[
                                                    Name(id='ValueError', ctx=Load()),
                                                    Name(id='AttributeError', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            name=None,
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='werkzeug', ctx=Load()),
                                                                attr='exceptions',
                                                                ctx=Load(),
                                                            ),
                                                            attr='HTTPException',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='description',
                                                                value=Constant(value='Cannot convert into barcode.', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                                Return(
                                    value=Call(
                                        func=Name(id='image_data_uri', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='base64', ctx=Load()),
                                                    attr='b64encode',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='barcode', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=None, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_available_qr_methods',
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
                            value=Constant(value=" Returns the QR-code generation methods that are available on this db,\n        in the form of a list of (code, name, sequence) elements, where\n        'code' is a unique string identifier, 'name' the name to display\n        to the user to designate the method, and 'sequence' is a positive integer\n        indicating the order in which those mehtods need to be checked, to avoid\n        shadowing between them (lower sequence means more prioritary).\n        ", kind=None),
                        ),
                        Return(
                            value=List(elts=[], ctx=Load()),
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
                    name='get_available_qr_methods_in_sequence',
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
                            value=Constant(value=' Same as _get_available_qr_methods but without returning the sequence,\n        and using it directly to order the returned list.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='all_available', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_available_qr_methods',
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
                                    value=Name(id='all_available', ctx=Load()),
                                    attr='sort',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='key',
                                        value=Lambda(
                                            args=arguments(
                                                posonlyargs=[],
                                                args=[arg(arg='x', annotation=None, type_comment=None)],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[],
                                            ),
                                            body=Subscript(
                                                value=Name(id='x', ctx=Load()),
                                                slice=Constant(value=2, kind=None),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=ListComp(
                                elt=Tuple(
                                    elts=[
                                        Name(id='code', ctx=Load()),
                                        Name(id='name', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='code', ctx=Store()),
                                                Name(id='name', ctx=Store()),
                                                Name(id='sequence', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Name(id='all_available', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
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
                    name='_eligible_for_qr_code',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='qr_method', annotation=None, type_comment=None),
                            arg(arg='debtor_partner', annotation=None, type_comment=None),
                            arg(arg='currency', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Tells whether or not the criteria to apply QR-generation\n        method qr_method are met for a payment on this account, in the\n        given currency, by debtor_partner. This does not impeach generation errors,\n        it only checks that this type of QR-code *should be* possible to generate.\n        Consistency of the required field needs then to be checked by _check_for_qr_code_errors().\n        ', kind=None),
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_for_qr_code_errors',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='qr_method', annotation=None, type_comment=None),
                            arg(arg='amount', annotation=None, type_comment=None),
                            arg(arg='currency', annotation=None, type_comment=None),
                            arg(arg='debtor_partner', annotation=None, type_comment=None),
                            arg(arg='free_communication', annotation=None, type_comment=None),
                            arg(arg='structured_communication', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Checks the data before generating a QR-code for the specified qr_method\n        (this method must have been checked for eligbility by _eligible_for_qr_code() first).\n\n        Returns None if no error was found, or a string describing the first error encountered\n        so that it can be reported to the user.\n        ', kind=None),
                        ),
                        Return(
                            value=Constant(value=None, kind=None),
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
