Module(
    body=[
        Import(
            names=[alias(name='re', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.models.res_bank',
            names=[alias(name='sanitize_account_number', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base_iban.models.res_partner_bank',
            names=[
                alias(name='normalize_iban', asname=None),
                alias(name='pretty_iban', asname=None),
                alias(name='validate_iban', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='ValidationError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.misc',
            names=[alias(name='mod10r', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='ISR_SUBSCRIPTION_CODE', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='CHF', kind=None),
                    Constant(value='EUR', kind=None),
                ],
                values=[
                    Constant(value='01', kind=None),
                    Constant(value='03', kind=None),
                ],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='CLEARING', ctx=Store())],
            value=Constant(value='09000', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_re_postal', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[Constant(value='^[0-9]{2}-[0-9]{1,6}-[0-9]$', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='_is_l10n_ch_postal',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='account_ref', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Returns True if the string account_ref is a valid postal account number,\n    i.e. it only contains ciphers and is last cipher is the result of a recursive\n    modulo 10 operation ran over the rest of it. Shorten form with - is also accepted.\n    ', kind=None),
                ),
                If(
                    test=Call(
                        func=Attribute(
                            value=Name(id='_re_postal', ctx=Load()),
                            attr='match',
                            ctx=Load(),
                        ),
                        args=[
                            BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='account_ref', ctx=Load()),
                                    Constant(value='', kind=None),
                                ],
                            ),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='ref_subparts', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='account_ref', ctx=Load()),
                                    attr='split',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='-', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='account_ref', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Subscript(
                                        value=Name(id='ref_subparts', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='ref_subparts', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='rjust',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=6, kind=None),
                                            Constant(value='0', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                op=Add(),
                                right=Subscript(
                                    value=Name(id='ref_subparts', ctx=Load()),
                                    slice=Constant(value=2, kind=None),
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='match',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='\\d+$', kind=None),
                            BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='account_ref', ctx=Load()),
                                    Constant(value='', kind=None),
                                ],
                            ),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='account_ref_without_check', ctx=Store())],
                            value=Subscript(
                                value=Name(id='account_ref', ctx=Load()),
                                slice=Slice(
                                    lower=None,
                                    upper=UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
                                    ),
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Compare(
                                left=Call(
                                    func=Name(id='mod10r', ctx=Load()),
                                    args=[Name(id='account_ref_without_check', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Name(id='account_ref', ctx=Load())],
                            ),
                        ),
                    ],
                    orelse=[],
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
            name='_is_l10n_ch_isr_issuer',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='account_ref', annotation=None, type_comment=None),
                    arg(arg='currency_code', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Returns True if the string account_ref is a valid a valid ISR issuer\n    An ISR issuer is postal account number that starts by 01 (CHF) or 03 (EUR),\n    ', kind=None),
                ),
                If(
                    test=Call(
                        func=Attribute(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='account_ref', ctx=Load()),
                                    Constant(value='', kind=None),
                                ],
                            ),
                            attr='startswith',
                            ctx=Load(),
                        ),
                        args=[
                            Subscript(
                                value=Name(id='ISR_SUBSCRIPTION_CODE', ctx=Load()),
                                slice=Name(id='currency_code', ctx=Load()),
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='_is_l10n_ch_postal', ctx=Load()),
                                args=[Name(id='account_ref', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
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
            name='validate_qr_iban',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='qr_iban', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Call(
                        func=Name(id='validate_iban', ctx=Load()),
                        args=[Name(id='qr_iban', ctx=Load())],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='sanitized_qr_iban', ctx=Store())],
                    value=Call(
                        func=Name(id='sanitize_account_number', ctx=Load()),
                        args=[Name(id='qr_iban', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Subscript(
                            value=Name(id='sanitized_qr_iban', ctx=Load()),
                            slice=Slice(
                                lower=None,
                                upper=Constant(value=2, kind=None),
                                step=None,
                            ),
                            ctx=Load(),
                        ),
                        ops=[NotEq()],
                        comparators=[Constant(value='CH', kind=None)],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='ValidationError', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='QR-IBAN numbers are only available in Switzerland.', kind=None)],
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
                            func=Name(id='check_qr_iban_range', ctx=Load()),
                            args=[Name(id='sanitized_qr_iban', ctx=Load())],
                            keywords=[],
                        ),
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='ValidationError', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Call(
                                            func=Name(id='_', ctx=Load()),
                                            args=[Constant(value="QR-IBAN '%s' is invalid.", kind=None)],
                                            keywords=[],
                                        ),
                                        op=Mod(),
                                        right=Name(id='qr_iban', ctx=Load()),
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
                    value=Constant(value=True, kind=None),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='check_qr_iban_range',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='iban', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                If(
                    test=BoolOp(
                        op=Or(),
                        values=[
                            UnaryOp(
                                op=Not(),
                                operand=Name(id='iban', ctx=Load()),
                            ),
                            Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='iban', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Lt()],
                                comparators=[Constant(value=9, kind=None)],
                            ),
                        ],
                    ),
                    body=[
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='iid_start_index', ctx=Store())],
                    value=Constant(value=4, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='iid_end_index', ctx=Store())],
                    value=Constant(value=8, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='iid', ctx=Store())],
                    value=Subscript(
                        value=Name(id='iban', ctx=Load()),
                        slice=Slice(
                            lower=Name(id='iid_start_index', ctx=Load()),
                            upper=BinOp(
                                left=Name(id='iid_end_index', ctx=Load()),
                                op=Add(),
                                right=Constant(value=1, kind=None),
                            ),
                            step=None,
                        ),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Return(
                    value=BoolOp(
                        op=And(),
                        values=[
                            Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='match',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='\\d+', kind=None),
                                    Name(id='iid', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            Compare(
                                left=Constant(value=30000, kind=None),
                                ops=[
                                    LtE(),
                                    LtE(),
                                ],
                                comparators=[
                                    Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[Name(id='iid', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=31999, kind=None),
                                ],
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
                Assign(
                    targets=[Name(id='l10n_ch_postal', ctx=Store())],
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
                                value=Constant(value='Swiss Postal Account', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_l10n_ch_postal', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='This field is used for the Swiss postal account number on a vendor account and for the client number on your own account. The client number is mostly 6 numbers without -, while the postal account number can be e.g. 01-162-8', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_ch_qr_iban', ctx=Store())],
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
                                value=Constant(value='QR-IBAN', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_l10n_ch_qr_iban', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Put the QR-IBAN here for your own bank accounts.  That way, you can still use the main IBAN in the Account Number while you will see the QR-IBAN for the barcode.  ', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_ch_isr_subscription_chf', ctx=Store())],
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
                                value=Constant(value='CHF ISR Subscription Number', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The subscription number provided by the bank or Postfinance to identify the bank, used to generate ISR in CHF. eg. 01-162-8', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_ch_isr_subscription_eur', ctx=Store())],
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
                                value=Constant(value='EUR ISR Subscription Number', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The subscription number provided by the bank or Postfinance to identify the bank, used to generate ISR in EUR. eg. 03-162-5', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_ch_show_subscription', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_l10n_ch_show_subscription', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='company',
                                                    ctx=Load(),
                                                ),
                                                attr='account_fiscal_country_id',
                                                ctx=Load(),
                                            ),
                                            attr='code',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='CH', kind=None)],
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_is_isr_issuer',
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
                        Return(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Name(id='_is_l10n_ch_isr_issuer', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='l10n_ch_postal',
                                                ctx=Load(),
                                            ),
                                            Constant(value='CHF', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='_is_l10n_ch_isr_issuer', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='l10n_ch_postal',
                                                ctx=Load(),
                                            ),
                                            Constant(value='EUR', kind=None),
                                        ],
                                        keywords=[],
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
                    name='_check_postal_num',
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
                            value=Constant(value='Validate postal number format', kind=None),
                        ),
                        For(
                            target=Name(id='rec', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='rec', ctx=Load()),
                                                attr='l10n_ch_postal',
                                                ctx=Load(),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Name(id='_is_l10n_ch_postal', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='rec', ctx=Load()),
                                                            attr='l10n_ch_postal',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='rec', ctx=Load()),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='rec', ctx=Load()),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='ref_company_ids',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='ValidationError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='The postal number {} is not valid.\nIt must be a valid postal number format. eg. 10-8060-7', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    attr='format',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='rec', ctx=Load()),
                                                                        attr='l10n_ch_postal',
                                                                        ctx=Load(),
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
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='l10n_ch_postal', kind=None),
                                Constant(value='partner_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_subscription_num',
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
                            value=Constant(value='Validate ISR subscription number format\n        Subscription number can only starts with 01 or 03\n        ', kind=None),
                        ),
                        For(
                            target=Name(id='rec', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='currency', ctx=Store()),
                                    iter=List(
                                        elts=[
                                            Constant(value='CHF', kind=None),
                                            Constant(value='EUR', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='subscrip', ctx=Store())],
                                            value=IfExp(
                                                test=Compare(
                                                    left=Name(id='currency', ctx=Load()),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='CHF', kind=None)],
                                                ),
                                                body=Attribute(
                                                    value=Name(id='rec', ctx=Load()),
                                                    attr='l10n_ch_isr_subscription_chf',
                                                    ctx=Load(),
                                                ),
                                                orelse=Attribute(
                                                    value=Name(id='rec', ctx=Load()),
                                                    attr='l10n_ch_isr_subscription_eur',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='subscrip', ctx=Load()),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Name(id='_is_l10n_ch_isr_issuer', ctx=Load()),
                                                            args=[
                                                                Name(id='subscrip', ctx=Load()),
                                                                Name(id='currency', ctx=Load()),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='example', ctx=Store())],
                                                    value=IfExp(
                                                        test=Compare(
                                                            left=Name(id='currency', ctx=Load()),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='CHF', kind=None)],
                                                        ),
                                                        body=Constant(value='01-162-8', kind=None),
                                                        orelse=Constant(value='03-162-5', kind=None),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='ValidationError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='The ISR subcription {} for {} number is not valid.\nIt must starts with {} and we a valid postal number format. eg. {}', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    attr='format',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='subscrip', ctx=Load()),
                                                                    Name(id='currency', ctx=Load()),
                                                                    Subscript(
                                                                        value=Name(id='ISR_SUBSCRIPTION_CODE', ctx=Load()),
                                                                        slice=Name(id='currency', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='example', ctx=Load()),
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
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='l10n_ch_isr_subscription_chf', kind=None),
                                Constant(value='l10n_ch_isr_subscription_eur', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_l10n_ch_show_subscription',
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
                        For(
                            target=Name(id='bank', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='bank', ctx=Load()),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='bank', ctx=Load()),
                                                    attr='l10n_ch_show_subscription',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='bank', ctx=Load()),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='ref_company_ids',
                                                            ctx=Load(),
                                                        ),
                                                        attr='country_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='code',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='CH', kind=None)],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Attribute(
                                                value=Name(id='bank', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='bank', ctx=Load()),
                                                            attr='l10n_ch_show_subscription',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='bank', ctx=Load()),
                                                                    attr='company_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='account_fiscal_country_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='code',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='CH', kind=None)],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='bank', ctx=Load()),
                                                            attr='l10n_ch_show_subscription',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='company',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='account_fiscal_country_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='code',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='CH', kind=None)],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='partner_id', kind=None),
                                Constant(value='company_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_sanitized_acc_number',
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
                            targets=[Name(id='postal_banks', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='b', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='b', ctx=Load()),
                                                attr='acc_type',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='postal', kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='bank', ctx=Store()),
                            iter=Name(id='postal_banks', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='bank', ctx=Load()),
                                            attr='sanitized_acc_number',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='bank', ctx=Load()),
                                        attr='acc_number',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ResPartnerBank', ctx=Load()),
                                            BinOp(
                                                left=Name(id='self', ctx=Load()),
                                                op=Sub(),
                                                right=Name(id='postal_banks', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_compute_sanitized_acc_number',
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
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='acc_number', kind=None),
                                Constant(value='acc_type', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_l10n_ch_qr_iban',
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
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='validate_qr_iban', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='acc_number',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='valid_qr_iban', ctx=Store())],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='ValidationError', ctx=Load()),
                                            name=None,
                                            body=[
                                                Assign(
                                                    targets=[Name(id='valid_qr_iban', ctx=Store())],
                                                    value=Constant(value=False, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                                If(
                                    test=Name(id='valid_qr_iban', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='l10n_ch_qr_iban',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='sanitized_acc_number',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='l10n_ch_qr_iban',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=None, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='acc_number', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='vals', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='l10n_ch_qr_iban', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='validate_qr_iban', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='vals', ctx=Load()),
                                                slice=Constant(value='l10n_ch_qr_iban', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='l10n_ch_qr_iban', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='pretty_iban', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='normalize_iban', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='vals', ctx=Load()),
                                                        slice=Constant(value='l10n_ch_qr_iban', kind=None),
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
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
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='vals', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='l10n_ch_qr_iban', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='validate_qr_iban', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='vals', ctx=Load()),
                                                slice=Constant(value='l10n_ch_qr_iban', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='l10n_ch_qr_iban', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='pretty_iban', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='normalize_iban', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='vals', ctx=Load()),
                                                        slice=Constant(value='l10n_ch_qr_iban', kind=None),
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
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_supported_account_types',
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
                                        args=[
                                            Name(id='ResPartnerBank', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_supported_account_types',
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
                                            Constant(value='postal', kind=None),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Postal', kind=None)],
                                                keywords=[],
                                            ),
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
                FunctionDef(
                    name='retrieve_acc_type',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='acc_number', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Overridden method enabling the recognition of swiss postal bank\n        account numbers.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='acc_number_split', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='acc_number', ctx=Load()),
                                    Compare(
                                        left=Constant(value=' ', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='acc_number', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='acc_number_split', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='acc_number', ctx=Load()),
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value=' ', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Name(id='_is_l10n_ch_postal', ctx=Load()),
                                        args=[Name(id='acc_number', ctx=Load())],
                                        keywords=[],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='acc_number_split', ctx=Load()),
                                            Call(
                                                func=Name(id='_is_l10n_ch_postal', ctx=Load()),
                                                args=[Name(id='acc_number_split', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value='postal', kind=None),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[
                                                    Name(id='ResPartnerBank', ctx=Load()),
                                                    Name(id='self', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='retrieve_acc_type',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='acc_number', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
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
                    name='_compute_l10n_ch_postal',
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
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='acc_type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='iban', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='l10n_ch_postal',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_retrieve_l10n_ch_postal',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='sanitized_acc_number',
                                                        ctx=Load(),
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
                                                left=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='acc_type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='postal', kind=None)],
                                            ),
                                            body=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='record', ctx=Load()),
                                                                attr='acc_number',
                                                                ctx=Load(),
                                                            ),
                                                            Compare(
                                                                left=Constant(value=' ', kind=None),
                                                                ops=[In()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Name(id='record', ctx=Load()),
                                                                        attr='acc_number',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='record', ctx=Load()),
                                                                    attr='l10n_ch_postal',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Subscript(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='record', ctx=Load()),
                                                                            attr='acc_number',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='split',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value=' ', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='record', ctx=Load()),
                                                                    attr='l10n_ch_postal',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Attribute(
                                                                value=Name(id='record', ctx=Load()),
                                                                attr='acc_number',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='record', ctx=Load()),
                                                                        attr='partner_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Compare(
                                                                        left=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='record', ctx=Load()),
                                                                                attr='acc_number',
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
                                                                        comparators=[
                                                                            List(
                                                                                elts=[
                                                                                    Constant(value='01', kind=None),
                                                                                    Constant(value='03', kind=None),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='record', ctx=Load()),
                                                                            attr='acc_number',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Constant(value='{} {}', kind=None),
                                                                            attr='format',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='record', ctx=Load()),
                                                                                attr='acc_number',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='record', ctx=Load()),
                                                                                    attr='partner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='name',
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
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='acc_number', kind=None),
                                Constant(value='partner_id', kind=None),
                                Constant(value='acc_type', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_is_postfinance_iban',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='iban', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Postfinance IBAN have format\n        CHXX 0900 0XXX XXXX XXXX K\n        Where 09000 is the clearing number\n        ', kind=None),
                        ),
                        Return(
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='iban', ctx=Load()),
                                            attr='startswith',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='CH', kind=None)],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Subscript(
                                            value=Name(id='iban', ctx=Load()),
                                            slice=Slice(
                                                lower=Constant(value=4, kind=None),
                                                upper=Constant(value=9, kind=None),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Name(id='CLEARING', ctx=Load())],
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
                    name='_pretty_postal_num',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='number', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="format a postal account number or an ISR subscription number\n        as per specifications with '-' separators.\n        eg. 010001628 -> 01-162-8\n        ", kind=None),
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='match',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='^[0-9]{2}-[0-9]{1,6}-[0-9]$', kind=None),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='number', ctx=Load()),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Name(id='number', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='currency_code', ctx=Store())],
                            value=Subscript(
                                value=Name(id='number', ctx=Load()),
                                slice=Slice(
                                    lower=None,
                                    upper=Constant(value=2, kind=None),
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='middle_part', ctx=Store())],
                            value=Subscript(
                                value=Name(id='number', ctx=Load()),
                                slice=Slice(
                                    lower=Constant(value=2, kind=None),
                                    upper=UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
                                    ),
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='trailing_cipher', ctx=Store())],
                            value=Subscript(
                                value=Name(id='number', ctx=Load()),
                                slice=UnaryOp(
                                    op=USub(),
                                    operand=Constant(value=1, kind=None),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='middle_part', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='middle_part', ctx=Load()),
                                    attr='lstrip',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='0', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=BinOp(
                                    left=BinOp(
                                        left=BinOp(
                                            left=Name(id='currency_code', ctx=Load()),
                                            op=Add(),
                                            right=Constant(value='-', kind=None),
                                        ),
                                        op=Add(),
                                        right=Name(id='middle_part', ctx=Load()),
                                    ),
                                    op=Add(),
                                    right=Constant(value='-', kind=None),
                                ),
                                op=Add(),
                                right=Name(id='trailing_cipher', ctx=Load()),
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
                    name='_retrieve_l10n_ch_postal',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='iban', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Reads a swiss postal account number from a an IBAN and returns it as\n        a string. Returns None if no valid postal account number was found, or\n        the given iban was not from Swiss Postfinance.\n\n        CH09 0900 0000 1000 8060 7 -> 10-8060-7\n        ', kind=None),
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_is_postfinance_iban',
                                    ctx=Load(),
                                ),
                                args=[Name(id='iban', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_pretty_postal_num',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='iban', ctx=Load()),
                                                slice=Slice(
                                                    lower=UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=9, kind=None),
                                                    ),
                                                    upper=None,
                                                    step=None,
                                                ),
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
                    name='_l10n_ch_get_qr_vals',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
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
                        Assign(
                            targets=[Name(id='comment', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='free_communication', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='comment', ctx=Store())],
                                    value=IfExp(
                                        test=Compare(
                                            left=Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='free_communication', ctx=Load())],
                                                keywords=[],
                                            ),
                                            ops=[Gt()],
                                            comparators=[Constant(value=140, kind=None)],
                                        ),
                                        body=BinOp(
                                            left=Subscript(
                                                value=Name(id='free_communication', ctx=Load()),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=Constant(value=137, kind=None),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            op=Add(),
                                            right=Constant(value='...', kind=None),
                                        ),
                                        orelse=Name(id='free_communication', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='creditor_addr_1', ctx=Store()),
                                        Name(id='creditor_addr_2', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_partner_address_lines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='debtor_addr_1', ctx=Store()),
                                        Name(id='debtor_addr_2', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_partner_address_lines',
                                    ctx=Load(),
                                ),
                                args=[Name(id='debtor_partner', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='reference_type', ctx=Store())],
                            value=Constant(value='NON', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='reference', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='acc_number', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='sanitized_acc_number',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='l10n_ch_qr_iban',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='reference_type', ctx=Store())],
                                    value=Constant(value='QRR', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='reference', ctx=Store())],
                                    value=Name(id='structured_communication', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='acc_number', ctx=Store())],
                                    value=Call(
                                        func=Name(id='sanitize_account_number', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='l10n_ch_qr_iban',
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
                            targets=[Name(id='currency', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='currency', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Constant(value='SPC', kind=None),
                                    Constant(value='0200', kind=None),
                                    Constant(value='1', kind=None),
                                    Name(id='acc_number', ctx=Load()),
                                    Constant(value='K', kind=None),
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
                                            upper=Constant(value=70, kind=None),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    Name(id='creditor_addr_1', ctx=Load()),
                                    Name(id='creditor_addr_2', ctx=Load()),
                                    Constant(value='', kind=None),
                                    Constant(value='', kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            attr='country_id',
                                            ctx=Load(),
                                        ),
                                        attr='code',
                                        ctx=Load(),
                                    ),
                                    Constant(value='', kind=None),
                                    Constant(value='', kind=None),
                                    Constant(value='', kind=None),
                                    Constant(value='', kind=None),
                                    Constant(value='', kind=None),
                                    Constant(value='', kind=None),
                                    Constant(value='', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Constant(value='{:.2f}', kind=None),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='amount', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='currency', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='K', kind=None),
                                    Subscript(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='debtor_partner', ctx=Load()),
                                                attr='commercial_partner_id',
                                                ctx=Load(),
                                            ),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                        slice=Slice(
                                            lower=None,
                                            upper=Constant(value=70, kind=None),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    Name(id='debtor_addr_1', ctx=Load()),
                                    Name(id='debtor_addr_2', ctx=Load()),
                                    Constant(value='', kind=None),
                                    Constant(value='', kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='debtor_partner', ctx=Load()),
                                            attr='country_id',
                                            ctx=Load(),
                                        ),
                                        attr='code',
                                        ctx=Load(),
                                    ),
                                    Name(id='reference_type', ctx=Load()),
                                    Name(id='reference', ctx=Load()),
                                    Name(id='comment', ctx=Load()),
                                    Constant(value='EPD', kind=None),
                                ],
                                ctx=Load(),
                            ),
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
                        If(
                            test=Compare(
                                left=Name(id='qr_method', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='ch_qr', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_l10n_ch_get_qr_vals',
                                            ctx=Load(),
                                        ),
                                        args=[
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
                                comparators=[Constant(value='ch_qr', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='barcode_type', kind=None),
                                            Constant(value='width', kind=None),
                                            Constant(value='height', kind=None),
                                            Constant(value='quiet', kind=None),
                                            Constant(value='mask', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='QR', kind=None),
                                            Constant(value=256, kind=None),
                                            Constant(value=256, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value='ch_cross', kind=None),
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
                    name='_get_partner_address_lines',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='partner', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Returns a tuple of two elements containing the address lines to use\n        for this partner. Line 1 contains the street and number, line 2 contains\n        zip and city. Those two lines are limited to 70 characters\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='streets', ctx=Store())],
                            value=List(
                                elts=[
                                    Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='street',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='street2',
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='line_1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value=' ', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='filter', ctx=Load()),
                                        args=[
                                            Constant(value=None, kind=None),
                                            Name(id='streets', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='line_2', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='zip',
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Constant(value=' ', kind=None),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='partner', ctx=Load()),
                                    attr='city',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Subscript(
                                        value=Name(id='line_1', ctx=Load()),
                                        slice=Slice(
                                            lower=None,
                                            upper=Constant(value=70, kind=None),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='line_2', ctx=Load()),
                                        slice=Slice(
                                            lower=None,
                                            upper=Constant(value=70, kind=None),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_is_qr_reference',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='reference', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Checks whether the given reference is a QR-reference, i.e. it is\n        made of 27 digits, the 27th being a mod10r check on the 26 previous ones.\n        ', kind=None),
                        ),
                        Return(
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='reference', ctx=Load()),
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='reference', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=27, kind=None)],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='match',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='\\d+$', kind=None),
                                            Name(id='reference', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Name(id='reference', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[
                                            Call(
                                                func=Name(id='mod10r', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='reference', ctx=Load()),
                                                        slice=Slice(
                                                            lower=None,
                                                            upper=UnaryOp(
                                                                op=USub(),
                                                                operand=Constant(value=1, kind=None),
                                                            ),
                                                            step=None,
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
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
                        If(
                            test=Compare(
                                left=Name(id='qr_method', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='ch_qr', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=BoolOp(
                                        op=And(),
                                        values=[
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
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='country_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='code',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='CH', kind=None)],
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='debtor_partner', ctx=Load()),
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='debtor_partner', ctx=Load()),
                                                                attr='country_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='code',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='CH', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='currency', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='EUR', kind=None),
                                                            Constant(value='CHF', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                        FunctionDef(
                            name='_partner_fields_set',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='partner', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Return(
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='zip',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='city',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='country_id',
                                                    ctx=Load(),
                                                ),
                                                attr='code',
                                                ctx=Load(),
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='partner', ctx=Load()),
                                                        attr='street',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='partner', ctx=Load()),
                                                        attr='street2',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='qr_method', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='ch_qr', kind=None)],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id='_partner_fields_set', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='The partner set on the bank account meant to receive the payment (%s) must have a complete postal address (street, zip, city and country).', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='acc_number',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='debtor_partner', ctx=Load()),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Name(id='_partner_fields_set', ctx=Load()),
                                                    args=[Name(id='debtor_partner', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='The partner must have a complete postal address (street, zip, city and country).', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='l10n_ch_qr_iban',
                                                ctx=Load(),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_is_qr_reference',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='structured_communication', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='When using a QR-IBAN as the destination account of a QR-code, the payment reference must be a QR-reference.', kind=None)],
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
                                            Constant(value='ch_qr', kind=None),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Swiss QR bill', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value=10, kind=None),
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
