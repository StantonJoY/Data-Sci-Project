Module(
    body=[
        Import(
            names=[alias(name='sys', asname=None)],
        ),
        Assign(
            targets=[Name(id='LOG_NOTSET', ctx=Store())],
            value=Constant(value='notset', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='LOG_DEBUG', ctx=Store())],
            value=Constant(value='debug', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='LOG_INFO', ctx=Store())],
            value=Constant(value='info', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='LOG_WARNING', ctx=Store())],
            value=Constant(value='warn', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='LOG_ERROR', ctx=Store())],
            value=Constant(value='error', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='LOG_CRITICAL', ctx=Store())],
            value=Constant(value='critical', kind=None),
            type_comment=None,
        ),
        FunctionDef(
            name='get_encodings',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='hint_encoding', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value='utf-8', kind=None)],
            ),
            body=[
                Assign(
                    targets=[Name(id='fallbacks', ctx=Store())],
                    value=Dict(
                        keys=[
                            Constant(value='latin1', kind=None),
                            Constant(value='iso-8859-1', kind=None),
                            Constant(value='iso-8859-8-i', kind=None),
                            Constant(value='cp1252', kind=None),
                        ],
                        values=[
                            Constant(value='latin9', kind=None),
                            Constant(value='iso8859-15', kind=None),
                            Constant(value='iso8859-8', kind=None),
                            Constant(value='1252', kind=None),
                        ],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='hint_encoding', ctx=Load()),
                    body=[
                        Expr(
                            value=Yield(
                                value=Name(id='hint_encoding', ctx=Load()),
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='hint_encoding', ctx=Load()),
                                        attr='lower',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ops=[In()],
                                comparators=[Name(id='fallbacks', ctx=Load())],
                            ),
                            body=[
                                Expr(
                                    value=Yield(
                                        value=Subscript(
                                            value=Name(id='fallbacks', ctx=Load()),
                                            slice=Call(
                                                func=Attribute(
                                                    value=Name(id='hint_encoding', ctx=Load()),
                                                    attr='lower',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                ),
                For(
                    target=Name(id='charset', ctx=Store()),
                    iter=List(
                        elts=[
                            Constant(value='utf8', kind=None),
                            Constant(value='latin1', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='hint_encoding', ctx=Load()),
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='charset', ctx=Load()),
                                                attr='lower',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ops=[NotEq()],
                                        comparators=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='hint_encoding', ctx=Load()),
                                                    attr='lower',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Yield(
                                        value=Name(id='charset', ctx=Load()),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                ImportFrom(
                    module='locale',
                    names=[alias(name='getpreferredencoding', asname=None)],
                    level=0,
                ),
                Assign(
                    targets=[Name(id='prefenc', ctx=Store())],
                    value=Call(
                        func=Name(id='getpreferredencoding', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Name(id='prefenc', ctx=Load()),
                            Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='prefenc', ctx=Load()),
                                        attr='lower',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='utf-8', kind=None)],
                            ),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Yield(
                                value=Name(id='prefenc', ctx=Load()),
                            ),
                        ),
                        Assign(
                            targets=[Name(id='prefenc', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='fallbacks', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='prefenc', ctx=Load()),
                                            attr='lower',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='prefenc', ctx=Load()),
                            body=[
                                Expr(
                                    value=Yield(
                                        value=Name(id='prefenc', ctx=Load()),
                                    ),
                                ),
                            ],
                            orelse=[],
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
            targets=[Name(id='text_type', ctx=Store())],
            value=Call(
                func=Name(id='type', ctx=Load()),
                args=[Constant(value='', kind='u')],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='ustr',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='value', annotation=None, type_comment=None),
                    arg(arg='hint_encoding', annotation=None, type_comment=None),
                    arg(arg='errors', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value='utf-8', kind=None),
                    Constant(value='strict', kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value="This method is similar to the builtin `unicode`, except\n    that it may try multiple encodings to find one that works\n    for decoding `value`, and defaults to 'utf-8' first.\n\n    :param value: the value to convert\n    :param hint_encoding: an optional encoding that was detected\n        upstream and should be tried first to decode ``value``.\n    :param str errors: optional `errors` flag to pass to the unicode\n        built-in to indicate how illegal character values should be\n        treated when converting a string: 'strict', 'ignore' or 'replace'\n        (see ``unicode()`` constructor).\n        Passing anything other than 'strict' means that the first\n        encoding tried will be used, even if it's not the correct\n        one to use, so be careful! Ignored if value is not a string/unicode.\n    :raise: UnicodeError if value cannot be coerced to unicode\n    :return: unicode string representing the given value\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='ttype', ctx=Store())],
                    value=Call(
                        func=Name(id='type', ctx=Load()),
                        args=[Name(id='value', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Name(id='ttype', ctx=Load()),
                        ops=[Is()],
                        comparators=[Name(id='text_type', ctx=Load())],
                    ),
                    body=[
                        Return(
                            value=Name(id='value', ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=BoolOp(
                        op=Or(),
                        values=[
                            Compare(
                                left=Name(id='ttype', ctx=Load()),
                                ops=[Is()],
                                comparators=[Name(id='bytes', ctx=Load())],
                            ),
                            Call(
                                func=Name(id='issubclass', ctx=Load()),
                                args=[
                                    Name(id='ttype', ctx=Load()),
                                    Name(id='bytes', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ],
                    ),
                    body=[
                        Try(
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='value', ctx=Load()),
                                            attr='decode',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='hint_encoding', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='errors',
                                                value=Name(id='errors', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name=None,
                                    body=[Pass()],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        For(
                            target=Name(id='ln', ctx=Store()),
                            iter=Call(
                                func=Name(id='get_encodings', ctx=Load()),
                                args=[Name(id='hint_encoding', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Try(
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='value', ctx=Load()),
                                                    attr='decode',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='ln', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='errors',
                                                        value=Name(id='errors', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name=None,
                                            body=[Pass()],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='value', ctx=Load()),
                            Name(id='Exception', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='exception_to_unicode', ctx=Load()),
                                args=[Name(id='value', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Try(
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='text_type', ctx=Load()),
                                args=[Name(id='value', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='Exception', ctx=Load()),
                            name=None,
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UnicodeError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='unable to convert %r', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[Name(id='value', ctx=Load())],
                                                    ctx=Load(),
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
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='exception_to_unicode',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='e', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                If(
                    test=Call(
                        func=Name(id='getattr', ctx=Load()),
                        args=[
                            Name(id='e', ctx=Load()),
                            Constant(value='args', kind=None),
                            Tuple(elts=[], ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='\n', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    GeneratorExp(
                                        elt=Call(
                                            func=Name(id='ustr', ctx=Load()),
                                            args=[Name(id='a', ctx=Load())],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='a', ctx=Store()),
                                                iter=Attribute(
                                                    value=Name(id='e', ctx=Load()),
                                                    attr='args',
                                                    ctx=Load(),
                                                ),
                                                ifs=[],
                                                is_async=0,
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
                Try(
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='text_type', ctx=Load()),
                                args=[Name(id='e', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='Exception', ctx=Load()),
                            name=None,
                            body=[
                                Return(
                                    value=Constant(value='Unknown message', kind='u'),
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
    type_ignores=[],
)
