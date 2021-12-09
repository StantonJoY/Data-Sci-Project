Module(
    body=[
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='datetime', asname=None)],
        ),
        Import(
            names=[alias(name='calendar', asname=None)],
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
            names=[alias(name='ValidationError', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='FNC1_CHAR', ctx=Store())],
            value=Constant(value='\x1d', kind=None),
            type_comment=None,
        ),
        ClassDef(
            name='BarcodeNomenclature',
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
                    value=Constant(value='barcode.nomenclature', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='is_gs1_nomenclature', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Is GS1 Nomenclature', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='This Nomenclature use the GS1 specification, only GS1-128 encoding rules is accepted is this kind of nomenclature.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='gs1_separator_fnc1', ctx=Store())],
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
                                value=Constant(value='FNC1 Seperator', kind=None),
                            ),
                            keyword(
                                arg='trim',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Alternative regex delimiter for the FNC1 (by default, if not set, it is <GS> ASCII 29 char). The seperator must not match the begin/end of any related rules pattern.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_pattern',
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
                            target=Name(id='nom', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='nom', ctx=Load()),
                                                attr='is_gs1_nomenclature',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='nom', ctx=Load()),
                                                attr='gs1_separator_fnc1',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Try(
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='re', ctx=Load()),
                                                            attr='compile',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='(?:%s)?', kind=None),
                                                                op=Mod(),
                                                                right=Attribute(
                                                                    value=Name(id='nom', ctx=Load()),
                                                                    attr='gs1_separator_fnc1',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Attribute(
                                                        value=Name(id='re', ctx=Load()),
                                                        attr='error',
                                                        ctx=Load(),
                                                    ),
                                                    name='error',
                                                    body=[
                                                        Raise(
                                                            exc=Call(
                                                                func=Name(id='ValidationError', ctx=Load()),
                                                                args=[
                                                                    BinOp(
                                                                        left=Call(
                                                                            func=Name(id='_', ctx=Load()),
                                                                            args=[Constant(value='The FNC1 Seperator Alternative is not a valid Regex: ', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        op=Add(),
                                                                        right=Call(
                                                                            func=Name(id='str', ctx=Load()),
                                                                            args=[Name(id='error', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
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
                            args=[Constant(value='gs1_separator_fnc1', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='gs1_date_to_date',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='gs1_date', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Converts a GS1 date into a datetime.date.\n\n        :param gs1_date: A year formated as yymmdd\n        :type gs1_date: str\n        :return: converted date\n        :rtype: datetime.date\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='now', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='datetime', ctx=Load()),
                                        attr='date',
                                        ctx=Load(),
                                    ),
                                    attr='today',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='current_century', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='now', ctx=Load()),
                                    attr='year',
                                    ctx=Load(),
                                ),
                                op=FloorDiv(),
                                right=Constant(value=100, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='substract_year', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Name(id='int', ctx=Load()),
                                    args=[
                                        Subscript(
                                            value=Name(id='gs1_date', ctx=Load()),
                                            slice=Slice(
                                                lower=Constant(value=0, kind=None),
                                                upper=Constant(value=2, kind=None),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                op=Sub(),
                                right=BinOp(
                                    left=Attribute(
                                        value=Name(id='now', ctx=Load()),
                                        attr='year',
                                        ctx=Load(),
                                    ),
                                    op=Mod(),
                                    right=Constant(value=100, kind=None),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='century', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Constant(value=51, kind=None),
                                                ops=[
                                                    LtE(),
                                                    LtE(),
                                                ],
                                                comparators=[
                                                    Name(id='substract_year', ctx=Load()),
                                                    Constant(value=99, kind=None),
                                                ],
                                            ),
                                            BinOp(
                                                left=Name(id='current_century', ctx=Load()),
                                                op=Sub(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=UnaryOp(
                                                    op=USub(),
                                                    operand=Constant(value=99, kind=None),
                                                ),
                                                ops=[
                                                    LtE(),
                                                    LtE(),
                                                ],
                                                comparators=[
                                                    Name(id='substract_year', ctx=Load()),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=50, kind=None),
                                                    ),
                                                ],
                                            ),
                                            BinOp(
                                                left=Name(id='current_century', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                        ],
                                    ),
                                    Name(id='current_century', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='year', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Name(id='century', ctx=Load()),
                                    op=Mult(),
                                    right=Constant(value=100, kind=None),
                                ),
                                op=Add(),
                                right=Call(
                                    func=Name(id='int', ctx=Load()),
                                    args=[
                                        Subscript(
                                            value=Name(id='gs1_date', ctx=Load()),
                                            slice=Slice(
                                                lower=Constant(value=0, kind=None),
                                                upper=Constant(value=2, kind=None),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Name(id='gs1_date', ctx=Load()),
                                    slice=Slice(
                                        lower=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=2, kind=None),
                                        ),
                                        upper=None,
                                        step=None,
                                    ),
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='00', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='date', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='datetime', ctx=Load()),
                                                attr='datetime',
                                                ctx=Load(),
                                            ),
                                            attr='strptime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Call(
                                                    func=Name(id='str', ctx=Load()),
                                                    args=[Name(id='year', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Subscript(
                                                    value=Name(id='gs1_date', ctx=Load()),
                                                    slice=Slice(
                                                        lower=Constant(value=2, kind=None),
                                                        upper=Constant(value=4, kind=None),
                                                        step=None,
                                                    ),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Constant(value='%Y%m', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='date', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='date', ctx=Load()),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='day',
                                                value=Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='calendar', ctx=Load()),
                                                            attr='monthrange',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='year', ctx=Load()),
                                                            Call(
                                                                func=Name(id='int', ctx=Load()),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='gs1_date', ctx=Load()),
                                                                        slice=Slice(
                                                                            lower=Constant(value=2, kind=None),
                                                                            upper=Constant(value=4, kind=None),
                                                                            step=None,
                                                                        ),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    slice=Constant(value=1, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='date', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='datetime', ctx=Load()),
                                                attr='datetime',
                                                ctx=Load(),
                                            ),
                                            attr='strptime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Call(
                                                    func=Name(id='str', ctx=Load()),
                                                    args=[Name(id='year', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Subscript(
                                                    value=Name(id='gs1_date', ctx=Load()),
                                                    slice=Slice(
                                                        lower=Constant(value=2, kind=None),
                                                        upper=None,
                                                        step=None,
                                                    ),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Constant(value='%Y%m%d', kind=None),
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
                                    value=Name(id='date', ctx=Load()),
                                    attr='date',
                                    ctx=Load(),
                                ),
                                args=[],
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
                    name='parse_gs1_rule_pattern',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='match', annotation=None, type_comment=None),
                            arg(arg='rule', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='rule', kind=None),
                                    Constant(value='ai', kind=None),
                                    Constant(value='string_value', kind=None),
                                ],
                                values=[
                                    Name(id='rule', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='match', ctx=Load()),
                                            attr='group',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=1, kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='match', ctx=Load()),
                                            attr='group',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=2, kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='rule', ctx=Load()),
                                    attr='gs1_content_type',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='measure', kind=None)],
                            ),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='decimal_position', ctx=Store())],
                                            value=Constant(value=0, kind=None),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Name(id='rule', ctx=Load()),
                                                attr='gs1_decimal_usage',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='decimal_position', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='match', ctx=Load()),
                                                                        attr='group',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value=1, kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                slice=UnaryOp(
                                                                    op=USub(),
                                                                    operand=Constant(value=1, kind=None),
                                                                ),
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
                                        If(
                                            test=Compare(
                                                left=Name(id='decimal_position', ctx=Load()),
                                                ops=[Gt()],
                                                comparators=[Constant(value=0, kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='result', ctx=Load()),
                                                            slice=Constant(value='value', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Name(id='float', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=BinOp(
                                                                    left=Subscript(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='match', ctx=Load()),
                                                                                attr='group',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Constant(value=2, kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        slice=Slice(
                                                                            lower=None,
                                                                            upper=UnaryOp(
                                                                                op=USub(),
                                                                                operand=Name(id='decimal_position', ctx=Load()),
                                                                            ),
                                                                            step=None,
                                                                        ),
                                                                        ctx=Load(),
                                                                    ),
                                                                    op=Add(),
                                                                    right=Constant(value='.', kind=None),
                                                                ),
                                                                op=Add(),
                                                                right=Subscript(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='match', ctx=Load()),
                                                                            attr='group',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value=2, kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    slice=Slice(
                                                                        lower=UnaryOp(
                                                                            op=USub(),
                                                                            operand=Name(id='decimal_position', ctx=Load()),
                                                                        ),
                                                                        upper=None,
                                                                        step=None,
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='result', ctx=Load()),
                                                            slice=Constant(value='value', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='match', ctx=Load()),
                                                                    attr='group',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value=2, kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name=None,
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='ValidationError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[
                                                                    Constant(value='There is something wrong with the barcode rule "%s" pattern.\nIf this rule uses decimal, check it can\'t get sometime else than a digit as last char for the Application Identifier.\nCheck also the possible matched values can only be digits, otherwise the value can\'t be casted as a measure.', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='rule', ctx=Load()),
                                                                        attr='name',
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
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='rule', ctx=Load()),
                                            attr='gs1_content_type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='identifier', kind=None)],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='match', ctx=Load()),
                                                            attr='group',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=2, kind=None)],
                                                        keywords=[],
                                                    ),
                                                    slice=UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1, kind=None),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='get_barcode_check_digit',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    BinOp(
                                                                        left=BinOp(
                                                                            left=Constant(value='0', kind=None),
                                                                            op=Mult(),
                                                                            right=BinOp(
                                                                                left=Constant(value=18, kind=None),
                                                                                op=Sub(),
                                                                                right=Call(
                                                                                    func=Name(id='len', ctx=Load()),
                                                                                    args=[
                                                                                        Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='match', ctx=Load()),
                                                                                                attr='group',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[Constant(value=2, kind=None)],
                                                                                            keywords=[],
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                            ),
                                                                        ),
                                                                        op=Add(),
                                                                        right=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='match', ctx=Load()),
                                                                                attr='group',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Constant(value=2, kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Return(
                                                    value=Constant(value=None, kind=None),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='result', ctx=Load()),
                                                    slice=Constant(value='value', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='match', ctx=Load()),
                                                    attr='group',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=2, kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='rule', ctx=Load()),
                                                    attr='gs1_content_type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='date', kind=None)],
                                            ),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='match', ctx=Load()),
                                                                        attr='group',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value=2, kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Constant(value=6, kind=None)],
                                                    ),
                                                    body=[
                                                        Return(
                                                            value=Constant(value=None, kind=None),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='result', ctx=Load()),
                                                            slice=Constant(value='value', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='gs1_date_to_date',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='match', ctx=Load()),
                                                                    attr='group',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value=2, kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='result', ctx=Load()),
                                                            slice=Constant(value='value', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='match', ctx=Load()),
                                                            attr='group',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=2, kind=None)],
                                                        keywords=[],
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
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='gs1_decompose_extanded',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='barcode', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Try to decompose the gs1 extanded barcode into several unit of information using gs1 rules.\n\n        Return a ordered list of dict\n        ', kind=None),
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
                        Assign(
                            targets=[Name(id='separator_group', ctx=Store())],
                            value=BinOp(
                                left=Name(id='FNC1_CHAR', ctx=Load()),
                                op=Add(),
                                right=Constant(value='?', kind=None),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='gs1_separator_fnc1',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='separator_group', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='(?:%s)?', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='gs1_separator_fnc1',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='results', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='gs1_rules', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='rule_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='r', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='r', ctx=Load()),
                                                attr='encoding',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='gs1-128', kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='find_next_rule',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='remaining_barcode', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                For(
                                    target=Name(id='rule', ctx=Store()),
                                    iter=Name(id='gs1_rules', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='match', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='re', ctx=Load()),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=BinOp(
                                                            left=Constant(value='^', kind=None),
                                                            op=Add(),
                                                            right=Attribute(
                                                                value=Name(id='rule', ctx=Load()),
                                                                attr='pattern',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        op=Add(),
                                                        right=Name(id='separator_group', ctx=Load()),
                                                    ),
                                                    Name(id='remaining_barcode', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='match', ctx=Load()),
                                                    Compare(
                                                        left=Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='match', ctx=Load()),
                                                                        attr='groups',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        ops=[GtE()],
                                                        comparators=[Constant(value=2, kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='res', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='parse_gs1_rule_pattern',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='match', ctx=Load()),
                                                            Name(id='rule', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='res', ctx=Load()),
                                                    body=[
                                                        Return(
                                                            value=Tuple(
                                                                elts=[
                                                                    Name(id='res', ctx=Load()),
                                                                    Subscript(
                                                                        value=Name(id='remaining_barcode', ctx=Load()),
                                                                        slice=Slice(
                                                                            lower=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='match', ctx=Load()),
                                                                                    attr='end',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[],
                                                                                keywords=[],
                                                                            ),
                                                                            upper=None,
                                                                            step=None,
                                                                        ),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
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
                                    value=Constant(value=None, kind=None),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        While(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='barcode', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Gt()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='res_bar', ctx=Store())],
                                    value=Call(
                                        func=Name(id='find_next_rule', ctx=Load()),
                                        args=[Name(id='barcode', ctx=Load())],
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
                                                operand=Name(id='res_bar', ctx=Load()),
                                            ),
                                            Compare(
                                                left=Subscript(
                                                    value=Name(id='res_bar', ctx=Load()),
                                                    slice=Constant(value=1, kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Name(id='barcode', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Constant(value=None, kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='barcode', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='res_bar', ctx=Load()),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='results', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='res_bar', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
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
                            value=Name(id='results', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='parse_barcode',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='barcode', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='is_gs1_nomenclature',
                                ctx=Load(),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='gs1_decompose_extanded',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='barcode', ctx=Load())],
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
                                    attr='parse_barcode',
                                    ctx=Load(),
                                ),
                                args=[Name(id='barcode', ctx=Load())],
                                keywords=[],
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
