Module(
    body=[
        ImportFrom(
            module='__future__',
            names=[alias(name='print_function', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='builtins', asname=None)],
        ),
        Import(
            names=[alias(name='math', asname=None)],
        ),
        FunctionDef(
            name='round',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='f', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='roundf', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='builtins', ctx=Load()),
                            attr='round',
                            ctx=Load(),
                        ),
                        args=[Name(id='f', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=BinOp(
                            left=Call(
                                func=Attribute(
                                    value=Name(id='builtins', ctx=Load()),
                                    attr='round',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Name(id='f', ctx=Load()),
                                        op=Add(),
                                        right=Constant(value=1, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                            op=Sub(),
                            right=Name(id='roundf', ctx=Load()),
                        ),
                        ops=[NotEq()],
                        comparators=[Constant(value=1, kind=None)],
                    ),
                    body=[
                        Return(
                            value=BinOp(
                                left=Name(id='f', ctx=Load()),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='math', ctx=Load()),
                                        attr='copysign',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value=0.5, kind=None),
                                        Name(id='f', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='math', ctx=Load()),
                            attr='copysign',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='roundf', ctx=Load()),
                            Name(id='f', ctx=Load()),
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
            name='_float_check_precision',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='precision_digits', annotation=None, type_comment=None),
                    arg(arg='precision_rounding', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                ],
            ),
            body=[
                Assert(
                    test=BoolOp(
                        op=And(),
                        values=[
                            BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Name(id='precision_digits', ctx=Load()),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    Compare(
                                        left=Name(id='precision_rounding', ctx=Load()),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                ],
                            ),
                            UnaryOp(
                                op=Not(),
                                operand=BoolOp(
                                    op=And(),
                                    values=[
                                        Name(id='precision_digits', ctx=Load()),
                                        Name(id='precision_rounding', ctx=Load()),
                                    ],
                                ),
                            ),
                        ],
                    ),
                    msg=Constant(value='exactly one of precision_digits and precision_rounding must be specified', kind=None),
                ),
                Assert(
                    test=BoolOp(
                        op=Or(),
                        values=[
                            Compare(
                                left=Name(id='precision_rounding', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            Compare(
                                left=Name(id='precision_rounding', ctx=Load()),
                                ops=[Gt()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                        ],
                    ),
                    msg=BinOp(
                        left=Constant(value='precision_rounding must be positive, got %s', kind=None),
                        op=Mod(),
                        right=Name(id='precision_rounding', ctx=Load()),
                    ),
                ),
                If(
                    test=Compare(
                        left=Name(id='precision_digits', ctx=Load()),
                        ops=[IsNot()],
                        comparators=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Return(
                            value=BinOp(
                                left=Constant(value=10, kind=None),
                                op=Pow(),
                                right=UnaryOp(
                                    op=USub(),
                                    operand=Name(id='precision_digits', ctx=Load()),
                                ),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='precision_rounding', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='float_round',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='value', annotation=None, type_comment=None),
                    arg(arg='precision_digits', annotation=None, type_comment=None),
                    arg(arg='precision_rounding', annotation=None, type_comment=None),
                    arg(arg='rounding_method', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value='HALF-UP', kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value="Return ``value`` rounded to ``precision_digits`` decimal digits,\n       minimizing IEEE-754 floating point representation errors, and applying\n       the tie-breaking rule selected with ``rounding_method``, by default\n       HALF-UP (away from zero).\n       Precision must be given by ``precision_digits`` or ``precision_rounding``,\n       not both!\n\n       :param float value: the value to round\n       :param int precision_digits: number of fractional digits to round to.\n       :param float precision_rounding: decimal number representing the minimum\n           non-zero value at the desired precision (for example, 0.01 for a \n           2-digit precision).\n       :param rounding_method: the rounding method used: 'HALF-UP', 'UP' or 'DOWN',\n           the first one rounding up to the closest number with the rule that\n           number>=0.5 is rounded up to 1, the second always rounding up and the\n           latest one always rounding down.\n       :return: rounded float\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='rounding_factor', ctx=Store())],
                    value=Call(
                        func=Name(id='_float_check_precision', ctx=Load()),
                        args=[],
                        keywords=[
                            keyword(
                                arg='precision_digits',
                                value=Name(id='precision_digits', ctx=Load()),
                            ),
                            keyword(
                                arg='precision_rounding',
                                value=Name(id='precision_rounding', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                If(
                    test=BoolOp(
                        op=Or(),
                        values=[
                            Compare(
                                left=Name(id='rounding_factor', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            Compare(
                                left=Name(id='value', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                        ],
                    ),
                    body=[
                        Return(
                            value=Constant(value=0.0, kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='normalized_value', ctx=Store())],
                    value=BinOp(
                        left=Name(id='value', ctx=Load()),
                        op=Div(),
                        right=Name(id='rounding_factor', ctx=Load()),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sign', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='math', ctx=Load()),
                            attr='copysign',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value=1.0, kind=None),
                            Name(id='normalized_value', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='epsilon_magnitude', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='math', ctx=Load()),
                            attr='log',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                func=Name(id='abs', ctx=Load()),
                                args=[Name(id='normalized_value', ctx=Load())],
                                keywords=[],
                            ),
                            Constant(value=2, kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='epsilon', ctx=Store())],
                    value=BinOp(
                        left=Constant(value=2, kind=None),
                        op=Pow(),
                        right=BinOp(
                            left=Name(id='epsilon_magnitude', ctx=Load()),
                            op=Sub(),
                            right=Constant(value=52, kind=None),
                        ),
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Name(id='rounding_method', ctx=Load()),
                        ops=[Eq()],
                        comparators=[Constant(value='UP', kind=None)],
                    ),
                    body=[
                        AugAssign(
                            target=Name(id='normalized_value', ctx=Store()),
                            op=Sub(),
                            value=BinOp(
                                left=Name(id='sign', ctx=Load()),
                                op=Mult(),
                                right=Name(id='epsilon', ctx=Load()),
                            ),
                        ),
                        Assign(
                            targets=[Name(id='rounded_value', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='math', ctx=Load()),
                                        attr='ceil',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='abs', ctx=Load()),
                                            args=[Name(id='normalized_value', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                op=Mult(),
                                right=Name(id='sign', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        If(
                            test=Compare(
                                left=Name(id='rounding_method', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='DOWN', kind=None)],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='normalized_value', ctx=Store()),
                                    op=Add(),
                                    value=BinOp(
                                        left=Name(id='sign', ctx=Load()),
                                        op=Mult(),
                                        right=Name(id='epsilon', ctx=Load()),
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='rounded_value', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='math', ctx=Load()),
                                                attr='floor',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Name(id='abs', ctx=Load()),
                                                    args=[Name(id='normalized_value', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Mult(),
                                        right=Name(id='sign', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                AugAssign(
                                    target=Name(id='normalized_value', ctx=Store()),
                                    op=Add(),
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='math', ctx=Load()),
                                            attr='copysign',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='epsilon', ctx=Load()),
                                            Name(id='normalized_value', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='rounded_value', ctx=Store())],
                                    value=Call(
                                        func=Name(id='round', ctx=Load()),
                                        args=[Name(id='normalized_value', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                    ],
                ),
                Assign(
                    targets=[Name(id='result', ctx=Store())],
                    value=BinOp(
                        left=Name(id='rounded_value', ctx=Load()),
                        op=Mult(),
                        right=Name(id='rounding_factor', ctx=Load()),
                    ),
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
            name='float_is_zero',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='value', annotation=None, type_comment=None),
                    arg(arg='precision_digits', annotation=None, type_comment=None),
                    arg(arg='precision_rounding', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value="Returns true if ``value`` is small enough to be treated as\n       zero at the given precision (smaller than the corresponding *epsilon*).\n       The precision (``10**-precision_digits`` or ``precision_rounding``)\n       is used as the zero *epsilon*: values less than that are considered\n       to be zero.\n       Precision must be given by ``precision_digits`` or ``precision_rounding``,\n       not both! \n\n       Warning: ``float_is_zero(value1-value2)`` is not equivalent to\n       ``float_compare(value1,value2) == 0``, as the former will round after\n       computing the difference, while the latter will round before, giving\n       different results for e.g. 0.006 and 0.002 at 2 digits precision. \n\n       :param int precision_digits: number of fractional digits to round to.\n       :param float precision_rounding: decimal number representing the minimum\n           non-zero value at the desired precision (for example, 0.01 for a \n           2-digit precision).\n       :param float value: value to compare with the precision's zero\n       :return: True if ``value`` is considered zero\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='epsilon', ctx=Store())],
                    value=Call(
                        func=Name(id='_float_check_precision', ctx=Load()),
                        args=[],
                        keywords=[
                            keyword(
                                arg='precision_digits',
                                value=Name(id='precision_digits', ctx=Load()),
                            ),
                            keyword(
                                arg='precision_rounding',
                                value=Name(id='precision_rounding', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Compare(
                        left=Call(
                            func=Name(id='abs', ctx=Load()),
                            args=[
                                Call(
                                    func=Name(id='float_round', ctx=Load()),
                                    args=[Name(id='value', ctx=Load())],
                                    keywords=[
                                        keyword(
                                            arg='precision_rounding',
                                            value=Name(id='epsilon', ctx=Load()),
                                        ),
                                    ],
                                ),
                            ],
                            keywords=[],
                        ),
                        ops=[Lt()],
                        comparators=[Name(id='epsilon', ctx=Load())],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='float_compare',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='value1', annotation=None, type_comment=None),
                    arg(arg='value2', annotation=None, type_comment=None),
                    arg(arg='precision_digits', annotation=None, type_comment=None),
                    arg(arg='precision_rounding', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value='Compare ``value1`` and ``value2`` after rounding them according to the\n       given precision. A value is considered lower/greater than another value\n       if their rounded value is different. This is not the same as having a\n       non-zero difference!\n       Precision must be given by ``precision_digits`` or ``precision_rounding``,\n       not both!\n\n       Example: 1.432 and 1.431 are equal at 2 digits precision,\n       so this method would return 0\n       However 0.006 and 0.002 are considered different (this method returns 1)\n       because they respectively round to 0.01 and 0.0, even though\n       0.006-0.002 = 0.004 which would be considered zero at 2 digits precision.\n\n       Warning: ``float_is_zero(value1-value2)`` is not equivalent to \n       ``float_compare(value1,value2) == 0``, as the former will round after\n       computing the difference, while the latter will round before, giving\n       different results for e.g. 0.006 and 0.002 at 2 digits precision. \n\n       :param int precision_digits: number of fractional digits to round to.\n       :param float precision_rounding: decimal number representing the minimum\n           non-zero value at the desired precision (for example, 0.01 for a \n           2-digit precision).\n       :param float value1: first value to compare\n       :param float value2: second value to compare\n       :return: (resp.) -1, 0 or 1, if ``value1`` is (resp.) lower than,\n           equal to, or greater than ``value2``, at the given precision.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='rounding_factor', ctx=Store())],
                    value=Call(
                        func=Name(id='_float_check_precision', ctx=Load()),
                        args=[],
                        keywords=[
                            keyword(
                                arg='precision_digits',
                                value=Name(id='precision_digits', ctx=Load()),
                            ),
                            keyword(
                                arg='precision_rounding',
                                value=Name(id='precision_rounding', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='value1', ctx=Store())],
                    value=Call(
                        func=Name(id='float_round', ctx=Load()),
                        args=[Name(id='value1', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='precision_rounding',
                                value=Name(id='rounding_factor', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='value2', ctx=Store())],
                    value=Call(
                        func=Name(id='float_round', ctx=Load()),
                        args=[Name(id='value2', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='precision_rounding',
                                value=Name(id='rounding_factor', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='delta', ctx=Store())],
                    value=BinOp(
                        left=Name(id='value1', ctx=Load()),
                        op=Sub(),
                        right=Name(id='value2', ctx=Load()),
                    ),
                    type_comment=None,
                ),
                If(
                    test=Call(
                        func=Name(id='float_is_zero', ctx=Load()),
                        args=[Name(id='delta', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='precision_rounding',
                                value=Name(id='rounding_factor', ctx=Load()),
                            ),
                        ],
                    ),
                    body=[
                        Return(
                            value=Constant(value=0, kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=IfExp(
                        test=Compare(
                            left=Name(id='delta', ctx=Load()),
                            ops=[Lt()],
                            comparators=[Constant(value=0.0, kind=None)],
                        ),
                        body=UnaryOp(
                            op=USub(),
                            operand=Constant(value=1, kind=None),
                        ),
                        orelse=Constant(value=1, kind=None),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='float_repr',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='value', annotation=None, type_comment=None),
                    arg(arg='precision_digits', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Returns a string representation of a float with the\n       the given number of fractional digits. This should not be\n       used to perform a rounding operation (this is done via\n       :meth:`~.float_round`), but only to produce a suitable\n       string representation for a float.\n\n        :param int precision_digits: number of fractional digits to\n                                     include in the output\n    ', kind=None),
                ),
                Return(
                    value=BinOp(
                        left=BinOp(
                            left=Constant(value='%%.%sf', kind=None),
                            op=Mod(),
                            right=Name(id='precision_digits', ctx=Load()),
                        ),
                        op=Mod(),
                        right=Name(id='value', ctx=Load()),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_float_repr', ctx=Store())],
            value=Name(id='float_repr', ctx=Load()),
            type_comment=None,
        ),
        FunctionDef(
            name='float_split_str',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='value', annotation=None, type_comment=None),
                    arg(arg='precision_digits', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value="Splits the given float 'value' in its unitary and decimal parts,\n       returning each of them as a string, rounding the value using\n       the provided ``precision_digits`` argument.\n\n       The length of the string returned for decimal places will always\n       be equal to ``precision_digits``, adding zeros at the end if needed.\n\n       In case ``precision_digits`` is zero, an empty string is returned for\n       the decimal places.\n\n       Examples:\n           1.432 with precision 2 => ('1', '43')\n           1.49  with precision 1 => ('1', '5')\n           1.1   with precision 3 => ('1', '100')\n           1.12  with precision 0 => ('1', '')\n\n       :param float value: value to split.\n       :param int precision_digits: number of fractional digits to round to.\n       :return: returns the tuple(<unitary part>, <decimal part>) of the given value\n       :rtype: tuple(str, str)\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='value', ctx=Store())],
                    value=Call(
                        func=Name(id='float_round', ctx=Load()),
                        args=[Name(id='value', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='precision_digits',
                                value=Name(id='precision_digits', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='value_repr', ctx=Store())],
                    value=Call(
                        func=Name(id='float_repr', ctx=Load()),
                        args=[
                            Name(id='value', ctx=Load()),
                            Name(id='precision_digits', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=IfExp(
                        test=Name(id='precision_digits', ctx=Load()),
                        body=Call(
                            func=Name(id='tuple', ctx=Load()),
                            args=[
                                Call(
                                    func=Attribute(
                                        value=Name(id='value_repr', ctx=Load()),
                                        attr='split',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='.', kind=None)],
                                    keywords=[],
                                ),
                            ],
                            keywords=[],
                        ),
                        orelse=Tuple(
                            elts=[
                                Name(id='value_repr', ctx=Load()),
                                Constant(value='', kind=None),
                            ],
                            ctx=Load(),
                        ),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='float_split',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='value', annotation=None, type_comment=None),
                    arg(arg='precision_digits', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' same as float_split_str() except that it returns the unitary and decimal\n        parts as integers instead of strings. In case ``precision_digits`` is zero,\n        0 is always returned as decimal part.\n\n       :rtype: tuple(int, int)\n    ', kind=None),
                ),
                Assign(
                    targets=[
                        Tuple(
                            elts=[
                                Name(id='units', ctx=Store()),
                                Name(id='cents', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        func=Name(id='float_split_str', ctx=Load()),
                        args=[
                            Name(id='value', ctx=Load()),
                            Name(id='precision_digits', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='cents', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=Tuple(
                                elts=[
                                    Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[Name(id='units', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Tuple(
                        elts=[
                            Call(
                                func=Name(id='int', ctx=Load()),
                                args=[Name(id='units', ctx=Load())],
                                keywords=[],
                            ),
                            Call(
                                func=Name(id='int', ctx=Load()),
                                args=[Name(id='cents', ctx=Load())],
                                keywords=[],
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
        If(
            test=Compare(
                left=Name(id='__name__', ctx=Load()),
                ops=[Eq()],
                comparators=[Constant(value='__main__', kind=None)],
            ),
            body=[
                Import(
                    names=[alias(name='time', asname=None)],
                ),
                Assign(
                    targets=[Name(id='start', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='time', ctx=Load()),
                            attr='time',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='count', ctx=Store())],
                    value=Constant(value=0, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='errors', ctx=Store())],
                    value=Constant(value=0, kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='try_round',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='amount', annotation=None, type_comment=None),
                            arg(arg='expected', annotation=None, type_comment=None),
                            arg(arg='precision_digits', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=3, kind=None)],
                    ),
                    body=[
                        Global(names=['count', 'errors']),
                        AugAssign(
                            target=Name(id='count', ctx=Store()),
                            op=Add(),
                            value=Constant(value=1, kind=None),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='float_repr', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='float_round', ctx=Load()),
                                        args=[Name(id='amount', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Name(id='precision_digits', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='precision_digits',
                                        value=Name(id='precision_digits', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='result', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[Name(id='expected', ctx=Load())],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='errors', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='print', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='###!!! Rounding error: got %s , expected %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='result', ctx=Load()),
                                                        Name(id='expected', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='fractions', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value=0.0, kind=None),
                            Constant(value=0.015, kind=None),
                            Constant(value=0.01499, kind=None),
                            Constant(value=0.675, kind=None),
                            Constant(value=0.67499, kind=None),
                            Constant(value=0.4555, kind=None),
                            Constant(value=0.4555, kind=None),
                            Constant(value=0.45555, kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='expecteds', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='.00', kind=None),
                            Constant(value='.02', kind=None),
                            Constant(value='.01', kind=None),
                            Constant(value='.68', kind=None),
                            Constant(value='.67', kind=None),
                            Constant(value='.46', kind=None),
                            Constant(value='.456', kind=None),
                            Constant(value='.4556', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='precisions', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value=2, kind=None),
                            Constant(value=2, kind=None),
                            Constant(value=2, kind=None),
                            Constant(value=2, kind=None),
                            Constant(value=2, kind=None),
                            Constant(value=2, kind=None),
                            Constant(value=3, kind=None),
                            Constant(value=4, kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='magnitude', ctx=Store()),
                    iter=Call(
                        func=Name(id='range', ctx=Load()),
                        args=[Constant(value=7, kind=None)],
                        keywords=[],
                    ),
                    body=[
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='frac', ctx=Store()),
                                    Name(id='exp', ctx=Store()),
                                    Name(id='prec', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='zip', ctx=Load()),
                                args=[
                                    Name(id='fractions', ctx=Load()),
                                    Name(id='expecteds', ctx=Load()),
                                    Name(id='precisions', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                For(
                                    target=Name(id='sign', ctx=Store()),
                                    iter=List(
                                        elts=[
                                            UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                            Constant(value=1, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    body=[
                                        For(
                                            target=Name(id='x', ctx=Store()),
                                            iter=Call(
                                                func=Name(id='range', ctx=Load()),
                                                args=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value=10000, kind=None),
                                                    Constant(value=97, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='n', ctx=Store())],
                                                    value=BinOp(
                                                        left=Name(id='x', ctx=Load()),
                                                        op=Mult(),
                                                        right=BinOp(
                                                            left=Constant(value=10, kind=None),
                                                            op=Pow(),
                                                            right=Name(id='magnitude', ctx=Load()),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='f', ctx=Store())],
                                                    value=BinOp(
                                                        left=Name(id='sign', ctx=Load()),
                                                        op=Mult(),
                                                        right=BinOp(
                                                            left=Name(id='n', ctx=Load()),
                                                            op=Add(),
                                                            right=Name(id='frac', ctx=Load()),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='f_exp', ctx=Store())],
                                                    value=BinOp(
                                                        left=BinOp(
                                                            left=IfExp(
                                                                test=BoolOp(
                                                                    op=And(),
                                                                    values=[
                                                                        Compare(
                                                                            left=Name(id='f', ctx=Load()),
                                                                            ops=[NotEq()],
                                                                            comparators=[Constant(value=0, kind=None)],
                                                                        ),
                                                                        Compare(
                                                                            left=Name(id='sign', ctx=Load()),
                                                                            ops=[Eq()],
                                                                            comparators=[
                                                                                UnaryOp(
                                                                                    op=USub(),
                                                                                    operand=Constant(value=1, kind=None),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                                body=Constant(value='-', kind=None),
                                                                orelse=Constant(value='', kind=None),
                                                            ),
                                                            op=Add(),
                                                            right=Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[Name(id='n', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        op=Add(),
                                                        right=Name(id='exp', ctx=Load()),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='try_round', ctx=Load()),
                                                        args=[
                                                            Name(id='f', ctx=Load()),
                                                            Name(id='f_exp', ctx=Load()),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='precision_digits',
                                                                value=Name(id='prec', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='stop', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='time', ctx=Load()),
                            attr='time',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Name(id='print', ctx=Load()),
                        args=[
                            Name(id='count', ctx=Load()),
                            Constant(value=' round calls, ', kind=None),
                            Name(id='errors', ctx=Load()),
                            Constant(value='errors, done in ', kind=None),
                            BinOp(
                                left=Name(id='stop', ctx=Load()),
                                op=Sub(),
                                right=Name(id='start', ctx=Load()),
                            ),
                            Constant(value='secs', kind=None),
                        ],
                        keywords=[],
                    ),
                ),
            ],
            orelse=[],
        ),
    ],
    type_ignores=[],
)
