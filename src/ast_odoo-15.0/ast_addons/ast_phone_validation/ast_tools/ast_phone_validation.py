Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[alias(name='_', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='logging', asname=None)],
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
        Assign(
            targets=[Name(id='_phonenumbers_lib_warning', ctx=Store())],
            value=Constant(value=False, kind=None),
            type_comment=None,
        ),
        Try(
            body=[
                Import(
                    names=[alias(name='phonenumbers', asname=None)],
                ),
                FunctionDef(
                    name='phone_parse',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='number', annotation=None, type_comment=None),
                            arg(arg='country_code', annotation=None, type_comment=None),
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
                                Assign(
                                    targets=[Name(id='phone_nbr', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='phonenumbers', ctx=Load()),
                                            attr='parse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='number', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='region',
                                                value=Name(id='country_code', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='keep_raw_input',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Attribute(
                                            value=Name(id='phonenumbers', ctx=Load()),
                                            attr='phonenumberutil',
                                            ctx=Load(),
                                        ),
                                        attr='NumberParseException',
                                        ctx=Load(),
                                    ),
                                    name='e',
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Unable to parse %(phone)s: %(error)s', kind=None)],
                                                        keywords=[
                                                            keyword(
                                                                arg='phone',
                                                                value=Name(id='number', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='error',
                                                                value=Call(
                                                                    func=Name(id='str', ctx=Load()),
                                                                    args=[Name(id='e', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ],
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='phonenumbers', ctx=Load()),
                                        attr='is_possible_number',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='phone_nbr', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='Impossible number %s: probably invalid number of digits.', kind=None),
                                                    Name(id='number', ctx=Load()),
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='phonenumbers', ctx=Load()),
                                        attr='is_valid_number',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='phone_nbr', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='Invalid number %s: probably incorrect prefix.', kind=None),
                                                    Name(id='number', ctx=Load()),
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
                        Return(
                            value=Name(id='phone_nbr', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='phone_format',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='number', annotation=None, type_comment=None),
                            arg(arg='country_code', annotation=None, type_comment=None),
                            arg(arg='country_phone_code', annotation=None, type_comment=None),
                            arg(arg='force_format', annotation=None, type_comment=None),
                            arg(arg='raise_exception', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value='INTERNATIONAL', kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Format the given phone number according to the localisation and international options.\n        :param number: number to convert\n        :param country_code: the ISO country code in two chars\n        :type country_code: str\n        :param country_phone_code: country dial in codes, defined by the ITU-T (Ex: 32 for Belgium)\n        :type country_phone_code: int\n        :param force_format: stringified version of format globals (see\n          https://github.com/daviddrysdale/python-phonenumbers/blob/dev/python/phonenumbers/phonenumberutil.py)\n            'E164' = 0\n            'INTERNATIONAL' = 1\n            'NATIONAL' = 2\n            'RFC3966' = 3\n        :type force_format: str\n        :rtype: str\n        ", kind=None),
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='phone_nbr', ctx=Store())],
                                    value=Call(
                                        func=Name(id='phone_parse', ctx=Load()),
                                        args=[
                                            Name(id='number', ctx=Load()),
                                            Name(id='country_code', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Tuple(
                                        elts=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='phonenumbers', ctx=Load()),
                                                    attr='phonenumberutil',
                                                    ctx=Load(),
                                                ),
                                                attr='NumberParseException',
                                                ctx=Load(),
                                            ),
                                            Name(id='UserError', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    name='e',
                                    body=[
                                        If(
                                            test=Name(id='raise_exception', ctx=Load()),
                                            body=[Raise(exc=None, cause=None)],
                                            orelse=[
                                                Return(
                                                    value=Name(id='number', ctx=Load()),
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='force_format', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='E164', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='phone_fmt', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='phonenumbers', ctx=Load()),
                                            attr='PhoneNumberFormat',
                                            ctx=Load(),
                                        ),
                                        attr='E164',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='force_format', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='RFC3966', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='phone_fmt', ctx=Store())],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='phonenumbers', ctx=Load()),
                                                    attr='PhoneNumberFormat',
                                                    ctx=Load(),
                                                ),
                                                attr='RFC3966',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='force_format', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='INTERNATIONAL', kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='phone_nbr', ctx=Load()),
                                                            attr='country_code',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Name(id='country_phone_code', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='phone_fmt', ctx=Store())],
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='phonenumbers', ctx=Load()),
                                                            attr='PhoneNumberFormat',
                                                            ctx=Load(),
                                                        ),
                                                        attr='INTERNATIONAL',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='phone_fmt', ctx=Store())],
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='phonenumbers', ctx=Load()),
                                                            attr='PhoneNumberFormat',
                                                            ctx=Load(),
                                                        ),
                                                        attr='NATIONAL',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='phonenumbers', ctx=Load()),
                                    attr='format_number',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='phone_nbr', ctx=Load()),
                                    Name(id='phone_fmt', ctx=Load()),
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
            handlers=[
                ExceptHandler(
                    type=Name(id='ImportError', ctx=Load()),
                    name=None,
                    body=[
                        FunctionDef(
                            name='phone_parse',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='number', annotation=None, type_comment=None),
                                    arg(arg='country_code', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='phone_format',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='number', annotation=None, type_comment=None),
                                    arg(arg='country_code', annotation=None, type_comment=None),
                                    arg(arg='country_phone_code', annotation=None, type_comment=None),
                                    arg(arg='force_format', annotation=None, type_comment=None),
                                    arg(arg='raise_exception', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[
                                    Constant(value='INTERNATIONAL', kind=None),
                                    Constant(value=True, kind=None),
                                ],
                            ),
                            body=[
                                Global(names=['_phonenumbers_lib_warning']),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='_phonenumbers_lib_warning', ctx=Load()),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='info',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='The `phonenumbers` Python module is not installed, contact numbers will not be verified. Please install the `phonenumbers` Python module.', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='_phonenumbers_lib_warning', ctx=Store())],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Name(id='number', ctx=Load()),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                    ],
                ),
            ],
            orelse=[],
            finalbody=[],
        ),
        FunctionDef(
            name='phone_sanitize_numbers',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='numbers', annotation=None, type_comment=None),
                    arg(arg='country_code', annotation=None, type_comment=None),
                    arg(arg='country_phone_code', annotation=None, type_comment=None),
                    arg(arg='force_format', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value='E164', kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value=" Given a list of numbers, return parsezd and sanitized information\n\n    :return dict: {number: {\n        'sanitized': sanitized and formated number or False (if cannot format)\n        'code': 'empty' (number was a void string), 'invalid' (error) or False (sanitize ok)\n        'msg': error message when 'invalid'\n    }}\n    ", kind=None),
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Call(
                            func=Name(id='isinstance', ctx=Load()),
                            args=[
                                Name(id='numbers', ctx=Load()),
                                Name(id='list', ctx=Load()),
                            ],
                            keywords=[],
                        ),
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='NotImplementedError', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='result', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='dict', ctx=Load()),
                            attr='fromkeys',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='numbers', ctx=Load()),
                            Constant(value=False, kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='number', ctx=Store()),
                    iter=Name(id='numbers', ctx=Load()),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='number', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='result', ctx=Load()),
                                            slice=Name(id='number', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Dict(
                                        keys=[
                                            Constant(value='sanitized', kind=None),
                                            Constant(value='code', kind=None),
                                            Constant(value='msg', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            Constant(value='empty', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Continue(),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='stripped', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='number', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='sanitized', ctx=Store())],
                                    value=Call(
                                        func=Name(id='phone_format', ctx=Load()),
                                        args=[
                                            Name(id='stripped', ctx=Load()),
                                            Name(id='country_code', ctx=Load()),
                                            Name(id='country_phone_code', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='force_format',
                                                value=Name(id='force_format', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='raise_exception',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name='e',
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='result', ctx=Load()),
                                                    slice=Name(id='number', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='sanitized', kind=None),
                                                    Constant(value='code', kind=None),
                                                    Constant(value='msg', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=False, kind=None),
                                                    Constant(value='invalid', kind=None),
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='e', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='result', ctx=Load()),
                                            slice=Name(id='number', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Dict(
                                        keys=[
                                            Constant(value='sanitized', kind=None),
                                            Constant(value='code', kind=None),
                                            Constant(value='msg', kind=None),
                                        ],
                                        values=[
                                            Name(id='sanitized', ctx=Load()),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            finalbody=[],
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Name(id='result', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='phone_sanitize_numbers_w_record',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='numbers', annotation=None, type_comment=None),
                    arg(arg='record', annotation=None, type_comment=None),
                    arg(arg='country', annotation=None, type_comment=None),
                    arg(arg='record_country_fname', annotation=None, type_comment=None),
                    arg(arg='force_format', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=False, kind=None),
                    Constant(value='country_id', kind=None),
                    Constant(value='E164', kind=None),
                ],
            ),
            body=[
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Call(
                            func=Name(id='isinstance', ctx=Load()),
                            args=[
                                Name(id='numbers', ctx=Load()),
                                Name(id='list', ctx=Load()),
                            ],
                            keywords=[],
                        ),
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='NotImplementedError', ctx=Load()),
                                args=[],
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
                        operand=Name(id='country', ctx=Load()),
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='record', ctx=Load()),
                                    Name(id='record_country_fname', ctx=Load()),
                                    Call(
                                        func=Name(id='hasattr', ctx=Load()),
                                        args=[
                                            Name(id='record', ctx=Load()),
                                            Name(id='record_country_fname', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Subscript(
                                        value=Name(id='record', ctx=Load()),
                                        slice=Name(id='record_country_fname', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='country', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='record', ctx=Load()),
                                        slice=Name(id='record_country_fname', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Name(id='record', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='country', ctx=Store())],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='company',
                                                    ctx=Load(),
                                                ),
                                                attr='country_id',
                                                ctx=Load(),
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
                Assign(
                    targets=[Name(id='country_code', ctx=Store())],
                    value=IfExp(
                        test=Name(id='country', ctx=Load()),
                        body=Attribute(
                            value=Name(id='country', ctx=Load()),
                            attr='code',
                            ctx=Load(),
                        ),
                        orelse=Constant(value=None, kind=None),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='country_phone_code', ctx=Store())],
                    value=IfExp(
                        test=Name(id='country', ctx=Load()),
                        body=Attribute(
                            value=Name(id='country', ctx=Load()),
                            attr='phone_code',
                            ctx=Load(),
                        ),
                        orelse=Constant(value=None, kind=None),
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Name(id='phone_sanitize_numbers', ctx=Load()),
                        args=[
                            Name(id='numbers', ctx=Load()),
                            Name(id='country_code', ctx=Load()),
                            Name(id='country_phone_code', ctx=Load()),
                        ],
                        keywords=[
                            keyword(
                                arg='force_format',
                                value=Name(id='force_format', ctx=Load()),
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
    type_ignores=[],
)
