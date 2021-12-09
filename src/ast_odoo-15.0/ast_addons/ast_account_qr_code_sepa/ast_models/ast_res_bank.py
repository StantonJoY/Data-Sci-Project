Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
                alias(name='api', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
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
                        If(
                            test=Compare(
                                left=Name(id='qr_method', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='sct_qr', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='comment', ctx=Store())],
                                    value=IfExp(
                                        test=UnaryOp(
                                            op=Not(),
                                            operand=Name(id='structured_communication', ctx=Load()),
                                        ),
                                        body=BoolOp(
                                            op=Or(),
                                            values=[
                                                Name(id='free_communication', ctx=Load()),
                                                Constant(value='', kind=None),
                                            ],
                                        ),
                                        orelse=Constant(value='', kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='qr_code_vals', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Constant(value='BCD', kind=None),
                                            Constant(value='002', kind=None),
                                            Constant(value='1', kind=None),
                                            Constant(value='SCT', kind=None),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='bank_bic',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            Subscript(
                                                value=BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='acc_holder_name',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=Constant(value=71, kind=None),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='sanitized_acc_number',
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='currency', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='str', ctx=Load()),
                                                    args=[Name(id='amount', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                            Constant(value='', kind=None),
                                            Subscript(
                                                value=BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Name(id='structured_communication', ctx=Load()),
                                                        Constant(value='', kind=None),
                                                    ],
                                                ),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=Constant(value=36, kind=None),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='comment', ctx=Load()),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=Constant(value=141, kind=None),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Name(id='qr_code_vals', ctx=Load()),
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
                                    attr='_get_qr_vals',
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
                        If(
                            test=Compare(
                                left=Name(id='qr_method', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='sct_qr', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='barcode_type', kind=None),
                                            Constant(value='width', kind=None),
                                            Constant(value='height', kind=None),
                                            Constant(value='humanreadable', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='QR', kind=None),
                                            Constant(value=128, kind=None),
                                            Constant(value=128, kind=None),
                                            Constant(value=1, kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Constant(value='\n', kind=None),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_get_qr_vals',
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
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
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
                        ),
                    ],
                    decorator_list=[],
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
                        If(
                            test=Compare(
                                left=Name(id='qr_method', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='sct_qr', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='sepa_country_codes', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
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
                                                    args=[Constant(value='base.sepa_zone', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='country_ids',
                                                ctx=Load(),
                                            ),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='code', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='non_iban_codes', ctx=Store())],
                                    value=Set(
                                        elts=[
                                            Constant(value='AX', kind=None),
                                            Constant(value='NC', kind=None),
                                            Constant(value='YT', kind=None),
                                            Constant(value='TF', kind=None),
                                            Constant(value='BL', kind=None),
                                            Constant(value='RE', kind=None),
                                            Constant(value='MF', kind=None),
                                            Constant(value='GP', kind=None),
                                            Constant(value='PM', kind=None),
                                            Constant(value='PF', kind=None),
                                            Constant(value='GF', kind=None),
                                            Constant(value='MQ', kind=None),
                                            Constant(value='JE', kind=None),
                                            Constant(value='GG', kind=None),
                                            Constant(value='IM', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='sepa_iban_codes', ctx=Store())],
                                    value=SetComp(
                                        elt=Name(id='code', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='code', ctx=Store()),
                                                iter=Name(id='sepa_country_codes', ctx=Load()),
                                                ifs=[
                                                    Compare(
                                                        left=Name(id='code', ctx=Load()),
                                                        ops=[NotIn()],
                                                        comparators=[Name(id='non_iban_codes', ctx=Load())],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='currency', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='EUR', kind=None)],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='acc_type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='iban', kind=None)],
                                            ),
                                            Compare(
                                                left=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='sanitized_acc_number',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Slice(
                                                        lower=None,
                                                        upper=Constant(value=2, kind=None),
                                                        step=None,
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[Name(id='sepa_iban_codes', ctx=Load())],
                                            ),
                                        ],
                                    ),
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
                                    attr='_eligible_for_qr_code',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='qr_method', ctx=Load()),
                                    Name(id='debtor_partner', ctx=Load()),
                                    Name(id='currency', ctx=Load()),
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
                        If(
                            test=Compare(
                                left=Name(id='qr_method', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='sct_qr', kind=None)],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='acc_holder_name',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='The account receiving the payment must have an account holder name or partner name set.', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
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
                                    attr='_check_for_qr_code_errors',
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
                        Assign(
                            targets=[Name(id='rslt', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
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
                                    value=Name(id='rslt', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Tuple(
                                        elts=[
                                            Constant(value='sct_qr', kind=None),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='SEPA Credit Transfer QR', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value=20, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='rslt', ctx=Load()),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
