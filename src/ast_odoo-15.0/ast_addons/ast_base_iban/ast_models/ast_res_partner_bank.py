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
            module='odoo.exceptions',
            names=[
                alias(name='UserError', asname=None),
                alias(name='ValidationError', asname=None),
            ],
            level=0,
        ),
        FunctionDef(
            name='normalize_iban',
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
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='sub',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='[\\W_]', kind=None),
                            Constant(value='', kind=None),
                            BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='iban', ctx=Load()),
                                    Constant(value='', kind=None),
                                ],
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
        FunctionDef(
            name='pretty_iban',
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
                Expr(
                    value=Constant(value=' return iban in groups of four characters separated by a single space ', kind=None),
                ),
                Try(
                    body=[
                        Expr(
                            value=Call(
                                func=Name(id='validate_iban', ctx=Load()),
                                args=[Name(id='iban', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='iban', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value=' ', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Subscript(
                                            value=Name(id='iban', ctx=Load()),
                                            slice=Slice(
                                                lower=Name(id='i', ctx=Load()),
                                                upper=BinOp(
                                                    left=Name(id='i', ctx=Load()),
                                                    op=Add(),
                                                    right=Constant(value=4, kind=None),
                                                ),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='i', ctx=Store()),
                                                iter=Call(
                                                    func=Name(id='range', ctx=Load()),
                                                    args=[
                                                        Constant(value=0, kind=None),
                                                        Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[Name(id='iban', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        Constant(value=4, kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='ValidationError', ctx=Load()),
                            name=None,
                            body=[Pass()],
                        ),
                    ],
                    orelse=[],
                    finalbody=[],
                ),
                Return(
                    value=Name(id='iban', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='get_bban_from_iban',
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
                Expr(
                    value=Constant(value=' Returns the basic bank account number corresponding to an IBAN.\n        Note : the BBAN is not the same as the domestic bank account number !\n        The relation between IBAN, BBAN and domestic can be found here : http://www.ecbs.org/iban.htm\n    ', kind=None),
                ),
                Return(
                    value=Subscript(
                        value=Call(
                            func=Name(id='normalize_iban', ctx=Load()),
                            args=[Name(id='iban', ctx=Load())],
                            keywords=[],
                        ),
                        slice=Slice(
                            lower=Constant(value=4, kind=None),
                            upper=None,
                            step=None,
                        ),
                        ctx=Load(),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='validate_iban',
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
                Assign(
                    targets=[Name(id='iban', ctx=Store())],
                    value=Call(
                        func=Name(id='normalize_iban', ctx=Load()),
                        args=[Name(id='iban', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='iban', ctx=Load()),
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='ValidationError', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='There is no IBAN code.', kind=None)],
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
                    targets=[Name(id='country_code', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Subscript(
                                value=Name(id='iban', ctx=Load()),
                                slice=Slice(
                                    lower=None,
                                    upper=Constant(value=2, kind=None),
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            attr='lower',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Name(id='country_code', ctx=Load()),
                        ops=[NotIn()],
                        comparators=[Name(id='_map_iban_template', ctx=Load())],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='ValidationError', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='The IBAN is invalid, it should begin with the country code', kind=None)],
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
                    targets=[Name(id='iban_template', ctx=Store())],
                    value=Subscript(
                        value=Name(id='_map_iban_template', ctx=Load()),
                        slice=Name(id='country_code', ctx=Load()),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Call(
                            func=Name(id='len', ctx=Load()),
                            args=[Name(id='iban', ctx=Load())],
                            keywords=[],
                        ),
                        ops=[NotEq()],
                        comparators=[
                            Call(
                                func=Name(id='len', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='iban_template', ctx=Load()),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=' ', kind=None),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
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
                                        left=Call(
                                            func=Name(id='_', ctx=Load()),
                                            args=[Constant(value='The IBAN does not seem to be correct. You should have entered something like this %s\nWhere B = National bank code, S = Branch code, C = Account No, k = Check digit', kind=None)],
                                            keywords=[],
                                        ),
                                        op=Mod(),
                                        right=Name(id='iban_template', ctx=Load()),
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
                    targets=[Name(id='check_chars', ctx=Store())],
                    value=BinOp(
                        left=Subscript(
                            value=Name(id='iban', ctx=Load()),
                            slice=Slice(
                                lower=Constant(value=4, kind=None),
                                upper=None,
                                step=None,
                            ),
                            ctx=Load(),
                        ),
                        op=Add(),
                        right=Subscript(
                            value=Name(id='iban', ctx=Load()),
                            slice=Slice(
                                lower=None,
                                upper=Constant(value=4, kind=None),
                                step=None,
                            ),
                            ctx=Load(),
                        ),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='digits', ctx=Store())],
                    value=Call(
                        func=Name(id='int', ctx=Load()),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Constant(value='', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    GeneratorExp(
                                        elt=Call(
                                            func=Name(id='str', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Name(id='int', ctx=Load()),
                                                    args=[
                                                        Name(id='char', ctx=Load()),
                                                        Constant(value=36, kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='char', ctx=Store()),
                                                iter=Name(id='check_chars', ctx=Load()),
                                                ifs=[],
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
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=BinOp(
                            left=Name(id='digits', ctx=Load()),
                            op=Mod(),
                            right=Constant(value=97, kind=None),
                        ),
                        ops=[NotEq()],
                        comparators=[Constant(value=1, kind=None)],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='ValidationError', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='This IBAN does not pass the validation check, please verify it.', kind=None)],
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
                                            Constant(value='iban', kind=None),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='IBAN', kind=None)],
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
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='validate_iban', ctx=Load()),
                                        args=[Name(id='acc_number', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Constant(value='iban', kind=None),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='ValidationError', ctx=Load()),
                                    name=None,
                                    body=[
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
                            orelse=[],
                            finalbody=[],
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
                    name='get_bban',
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
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='acc_type',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='iban', kind=None)],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Cannot compute the BBAN because the account number is not an IBAN.', kind=None)],
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
                        Return(
                            value=Call(
                                func=Name(id='get_bban_from_iban', ctx=Load()),
                                args=[
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals_list', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='vals', ctx=Store()),
                            iter=Name(id='vals_list', ctx=Load()),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='acc_number', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Try(
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='validate_iban', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='vals', ctx=Load()),
                                                                slice=Constant(value='acc_number', kind=None),
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
                                                            slice=Constant(value='acc_number', kind=None),
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
                                                                        slice=Constant(value='acc_number', kind=None),
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
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='ValidationError', ctx=Load()),
                                                    name=None,
                                                    body=[Pass()],
                                                ),
                                            ],
                                            orelse=[],
                                            finalbody=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals_list', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model_create_multi',
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
                                args=[Constant(value='acc_number', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='validate_iban', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='vals', ctx=Load()),
                                                        slice=Constant(value='acc_number', kind=None),
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
                                                    slice=Constant(value='acc_number', kind=None),
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
                                                                slice=Constant(value='acc_number', kind=None),
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
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='ValidationError', ctx=Load()),
                                            name=None,
                                            body=[Pass()],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
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
                    name='_check_iban',
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
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='bank', ctx=Load()),
                                            attr='acc_type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='iban', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='validate_iban', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='bank', ctx=Load()),
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
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
                    name='check_iban',
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
                        defaults=[Constant(value='', kind=None)],
                    ),
                    body=[
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='validate_iban', ctx=Load()),
                                        args=[Name(id='iban', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='ValidationError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Return(
                                            value=Constant(value=False, kind=None),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        Assign(
            targets=[Name(id='_map_iban_template', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='ad', kind=None),
                    Constant(value='ae', kind=None),
                    Constant(value='al', kind=None),
                    Constant(value='at', kind=None),
                    Constant(value='az', kind=None),
                    Constant(value='ba', kind=None),
                    Constant(value='be', kind=None),
                    Constant(value='bg', kind=None),
                    Constant(value='bh', kind=None),
                    Constant(value='br', kind=None),
                    Constant(value='by', kind=None),
                    Constant(value='ch', kind=None),
                    Constant(value='cr', kind=None),
                    Constant(value='cy', kind=None),
                    Constant(value='cz', kind=None),
                    Constant(value='de', kind=None),
                    Constant(value='dk', kind=None),
                    Constant(value='do', kind=None),
                    Constant(value='ee', kind=None),
                    Constant(value='es', kind=None),
                    Constant(value='fi', kind=None),
                    Constant(value='fo', kind=None),
                    Constant(value='fr', kind=None),
                    Constant(value='gb', kind=None),
                    Constant(value='ge', kind=None),
                    Constant(value='gi', kind=None),
                    Constant(value='gl', kind=None),
                    Constant(value='gr', kind=None),
                    Constant(value='gt', kind=None),
                    Constant(value='hr', kind=None),
                    Constant(value='hu', kind=None),
                    Constant(value='ie', kind=None),
                    Constant(value='il', kind=None),
                    Constant(value='is', kind=None),
                    Constant(value='it', kind=None),
                    Constant(value='jo', kind=None),
                    Constant(value='kw', kind=None),
                    Constant(value='kz', kind=None),
                    Constant(value='lb', kind=None),
                    Constant(value='li', kind=None),
                    Constant(value='lt', kind=None),
                    Constant(value='lu', kind=None),
                    Constant(value='lv', kind=None),
                    Constant(value='mc', kind=None),
                    Constant(value='md', kind=None),
                    Constant(value='me', kind=None),
                    Constant(value='mk', kind=None),
                    Constant(value='mr', kind=None),
                    Constant(value='mt', kind=None),
                    Constant(value='mu', kind=None),
                    Constant(value='nl', kind=None),
                    Constant(value='no', kind=None),
                    Constant(value='pk', kind=None),
                    Constant(value='pl', kind=None),
                    Constant(value='ps', kind=None),
                    Constant(value='pt', kind=None),
                    Constant(value='qa', kind=None),
                    Constant(value='ro', kind=None),
                    Constant(value='rs', kind=None),
                    Constant(value='sa', kind=None),
                    Constant(value='se', kind=None),
                    Constant(value='si', kind=None),
                    Constant(value='sk', kind=None),
                    Constant(value='sm', kind=None),
                    Constant(value='tn', kind=None),
                    Constant(value='tr', kind=None),
                    Constant(value='ua', kind=None),
                    Constant(value='vg', kind=None),
                    Constant(value='xk', kind=None),
                ],
                values=[
                    Constant(value='ADkk BBBB SSSS CCCC CCCC CCCC', kind=None),
                    Constant(value='AEkk BBBC CCCC CCCC CCCC CCC', kind=None),
                    Constant(value='ALkk BBBS SSSK CCCC CCCC CCCC CCCC', kind=None),
                    Constant(value='ATkk BBBB BCCC CCCC CCCC', kind=None),
                    Constant(value='AZkk BBBB CCCC CCCC CCCC CCCC CCCC', kind=None),
                    Constant(value='BAkk BBBS SSCC CCCC CCKK', kind=None),
                    Constant(value='BEkk BBBC CCCC CCXX', kind=None),
                    Constant(value='BGkk BBBB SSSS DDCC CCCC CC', kind=None),
                    Constant(value='BHkk BBBB CCCC CCCC CCCC CC', kind=None),
                    Constant(value='BRkk BBBB BBBB SSSS SCCC CCCC CCCT N', kind=None),
                    Constant(value='BYkk BBBB AAAA CCCC CCCC CCCC CCCC', kind=None),
                    Constant(value='CHkk BBBB BCCC CCCC CCCC C', kind=None),
                    Constant(value='CRkk BBBC CCCC CCCC CCCC CC', kind=None),
                    Constant(value='CYkk BBBS SSSS CCCC CCCC CCCC CCCC', kind=None),
                    Constant(value='CZkk BBBB SSSS SSCC CCCC CCCC', kind=None),
                    Constant(value='DEkk BBBB BBBB CCCC CCCC CC', kind=None),
                    Constant(value='DKkk BBBB CCCC CCCC CC', kind=None),
                    Constant(value='DOkk BBBB CCCC CCCC CCCC CCCC CCCC', kind=None),
                    Constant(value='EEkk BBSS CCCC CCCC CCCK', kind=None),
                    Constant(value='ESkk BBBB SSSS KKCC CCCC CCCC', kind=None),
                    Constant(value='FIkk BBBB BBCC CCCC CK', kind=None),
                    Constant(value='FOkk CCCC CCCC CCCC CC', kind=None),
                    Constant(value='FRkk BBBB BGGG GGCC CCCC CCCC CKK', kind=None),
                    Constant(value='GBkk BBBB SSSS SSCC CCCC CC', kind=None),
                    Constant(value='GEkk BBCC CCCC CCCC CCCC CC', kind=None),
                    Constant(value='GIkk BBBB CCCC CCCC CCCC CCC', kind=None),
                    Constant(value='GLkk BBBB CCCC CCCC CC', kind=None),
                    Constant(value='GRkk BBBS SSSC CCCC CCCC CCCC CCC', kind=None),
                    Constant(value='GTkk BBBB MMTT CCCC CCCC CCCC CCCC', kind=None),
                    Constant(value='HRkk BBBB BBBC CCCC CCCC C', kind=None),
                    Constant(value='HUkk BBBS SSSC CCCC CCCC CCCC CCCC', kind=None),
                    Constant(value='IEkk BBBB SSSS SSCC CCCC CC', kind=None),
                    Constant(value='ILkk BBBS SSCC CCCC CCCC CCC', kind=None),
                    Constant(value='ISkk BBBB SSCC CCCC XXXX XXXX XX', kind=None),
                    Constant(value='ITkk KBBB BBSS SSSC CCCC CCCC CCC', kind=None),
                    Constant(value='JOkk BBBB NNNN CCCC CCCC CCCC CCCC CC', kind=None),
                    Constant(value='KWkk BBBB CCCC CCCC CCCC CCCC CCCC CC', kind=None),
                    Constant(value='KZkk BBBC CCCC CCCC CCCC', kind=None),
                    Constant(value='LBkk BBBB CCCC CCCC CCCC CCCC CCCC', kind=None),
                    Constant(value='LIkk BBBB BCCC CCCC CCCC C', kind=None),
                    Constant(value='LTkk BBBB BCCC CCCC CCCC', kind=None),
                    Constant(value='LUkk BBBC CCCC CCCC CCCC', kind=None),
                    Constant(value='LVkk BBBB CCCC CCCC CCCC C', kind=None),
                    Constant(value='MCkk BBBB BGGG GGCC CCCC CCCC CKK', kind=None),
                    Constant(value='MDkk BBCC CCCC CCCC CCCC CCCC', kind=None),
                    Constant(value='MEkk BBBC CCCC CCCC CCCC KK', kind=None),
                    Constant(value='MKkk BBBC CCCC CCCC CKK', kind=None),
                    Constant(value='MRkk BBBB BSSS SSCC CCCC CCCC CKK', kind=None),
                    Constant(value='MTkk BBBB SSSS SCCC CCCC CCCC CCCC CCC', kind=None),
                    Constant(value='MUkk BBBB BBSS CCCC CCCC CCCC CCCC CC', kind=None),
                    Constant(value='NLkk BBBB CCCC CCCC CC', kind=None),
                    Constant(value='NOkk BBBB CCCC CCK', kind=None),
                    Constant(value='PKkk BBBB CCCC CCCC CCCC CCCC', kind=None),
                    Constant(value='PLkk BBBS SSSK CCCC CCCC CCCC CCCC', kind=None),
                    Constant(value='PSkk BBBB XXXX XXXX XCCC CCCC CCCC C', kind=None),
                    Constant(value='PTkk BBBB SSSS CCCC CCCC CCCK K', kind=None),
                    Constant(value='QAkk BBBB CCCC CCCC CCCC CCCC CCCC C', kind=None),
                    Constant(value='ROkk BBBB CCCC CCCC CCCC CCCC', kind=None),
                    Constant(value='RSkk BBBC CCCC CCCC CCCC KK', kind=None),
                    Constant(value='SAkk BBCC CCCC CCCC CCCC CCCC', kind=None),
                    Constant(value='SEkk BBBB CCCC CCCC CCCC CCCC', kind=None),
                    Constant(value='SIkk BBSS SCCC CCCC CKK', kind=None),
                    Constant(value='SKkk BBBB SSSS SSCC CCCC CCCC', kind=None),
                    Constant(value='SMkk KBBB BBSS SSSC CCCC CCCC CCC', kind=None),
                    Constant(value='TNkk BBSS SCCC CCCC CCCC CCCC', kind=None),
                    Constant(value='TRkk BBBB BRCC CCCC CCCC CCCC CC', kind=None),
                    Constant(value='UAkk BBBB BBCC CCCC CCCC CCCC CCCC C', kind=None),
                    Constant(value='VGkk BBBB CCCC CCCC CCCC CCCC', kind=None),
                    Constant(value='XKkk BBBB CCCC CCCC CCCC', kind=None),
                ],
            ),
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
