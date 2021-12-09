Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        Import(
            names=[alias(name='unittest', asname=None)],
        ),
        ImportFrom(
            module=None,
            names=[alias(name='sql_db', asname=None)],
            level=2,
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
        ClassDef(
            name='OdooTestResult',
            bases=[
                Attribute(
                    value=Attribute(
                        value=Name(id='unittest', ctx=Load()),
                        attr='result',
                        ctx=Load(),
                    ),
                    attr='TestResult',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='\n    This class in inspired from TextTestResult (https://github.com/python/cpython/blob/master/Lib/unittest/runner.py)\n    Instead of using a stream, we are using the logger,\n    but replacing the "findCaller" in order to give the information we\n    have based on the test object that is running.\n    ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
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
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='time_start',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='queries_start',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__str__',
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
                            value=JoinedStr(
                                values=[
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='failures',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                    Constant(value=' failed, ', kind=None),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='errors',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                    Constant(value=' error(s) of ', kind=None),
                                    FormattedValue(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='testsRun',
                                            ctx=Load(),
                                        ),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                    Constant(value=' tests', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='update',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='other', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Merges an other test result into this one, only updates contents\n\n        :type other: OdooTestResult\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='failures',
                                        ctx=Load(),
                                    ),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='other', ctx=Load()),
                                        attr='failures',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='errors',
                                        ctx=Load(),
                                    ),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='other', ctx=Load()),
                                        attr='errors',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        AugAssign(
                            target=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='testsRun',
                                ctx=Store(),
                            ),
                            op=Add(),
                            value=Attribute(
                                value=Name(id='other', ctx=Load()),
                                attr='testsRun',
                                ctx=Load(),
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='skipped',
                                        ctx=Load(),
                                    ),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='other', ctx=Load()),
                                        attr='skipped',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='expectedFailures',
                                        ctx=Load(),
                                    ),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='other', ctx=Load()),
                                        attr='expectedFailures',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='unexpectedSuccesses',
                                        ctx=Load(),
                                    ),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='other', ctx=Load()),
                                        attr='unexpectedSuccesses',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='shouldStop',
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='shouldStop',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='other', ctx=Load()),
                                        attr='shouldStop',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='log',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='level', annotation=None, type_comment=None),
                            arg(arg='msg', annotation=None, type_comment=None),
                        ],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[
                            arg(arg='test', annotation=None, type_comment=None),
                            arg(arg='exc_info', annotation=None, type_comment=None),
                            arg(arg='extra', annotation=None, type_comment=None),
                            arg(arg='stack_info', annotation=None, type_comment=None),
                            arg(arg='caller_infos', annotation=None, type_comment=None),
                        ],
                        kw_defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                        ],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        ``test`` is the running test case, ``caller_infos`` is\n        (fn, lno, func, sinfo) (logger.findCaller format), see logger.log for\n        the other parameters.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='test', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='test', ctx=Load()),
                                    Name(id='self', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='test', ctx=Load()),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='unittest', ctx=Load()),
                                                    attr='case',
                                                    ctx=Load(),
                                                ),
                                                attr='_SubTest',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='test', ctx=Load()),
                                        attr='test_case',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='test', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='test', ctx=Load()),
                                        attr='test_case',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='logger', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='logging', ctx=Load()),
                                    attr='getLogger',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='test', ctx=Load()),
                                        attr='__module__',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='caller_infos', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='caller_infos', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='logger', ctx=Load()),
                                                    attr='findCaller',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='stack_info', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='ValueError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Assign(
                                            targets=[Name(id='caller_infos', ctx=Store())],
                                            value=Tuple(
                                                elts=[
                                                    Constant(value='(unknown file)', kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value='(unknown function)', kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='fn', ctx=Store()),
                                        Name(id='lno', ctx=Store()),
                                        Name(id='func', ctx=Store()),
                                        Name(id='sinfo', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='caller_infos', ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='logger', ctx=Load()),
                                    attr='isEnabledFor',
                                    ctx=Load(),
                                ),
                                args=[Name(id='level', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='record', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='logger', ctx=Load()),
                                            attr='makeRecord',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='logger', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Name(id='level', ctx=Load()),
                                            Name(id='fn', ctx=Load()),
                                            Name(id='lno', ctx=Load()),
                                            Name(id='msg', ctx=Load()),
                                            Name(id='args', ctx=Load()),
                                            Name(id='exc_info', ctx=Load()),
                                            Name(id='func', ctx=Load()),
                                            Name(id='extra', ctx=Load()),
                                            Name(id='sinfo', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='logger', ctx=Load()),
                                            attr='handle',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='record', ctx=Load())],
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
                FunctionDef(
                    name='getDescription',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='test', annotation=None, type_comment=None),
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
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='test', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='unittest', ctx=Load()),
                                            attr='case',
                                            ctx=Load(),
                                        ),
                                        attr='_SubTest',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=BinOp(
                                        left=Constant(value='Subtest %s.%s %s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='test', ctx=Load()),
                                                            attr='test_case',
                                                            ctx=Load(),
                                                        ),
                                                        attr='__class__',
                                                        ctx=Load(),
                                                    ),
                                                    attr='__qualname__',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='test', ctx=Load()),
                                                        attr='test_case',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_testMethodName',
                                                    ctx=Load(),
                                                ),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='test', ctx=Load()),
                                                        attr='_subDescription',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='test', ctx=Load()),
                                    Attribute(
                                        value=Name(id='unittest', ctx=Load()),
                                        attr='TestCase',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=BinOp(
                                        left=Constant(value='%s.%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='test', ctx=Load()),
                                                        attr='__class__',
                                                        ctx=Load(),
                                                    ),
                                                    attr='__qualname__',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='test', ctx=Load()),
                                                    attr='_testMethodName',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Name(id='str', ctx=Load()),
                                args=[Name(id='test', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='startTest',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='test', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='startTest',
                                    ctx=Load(),
                                ),
                                args=[Name(id='test', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='log',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='logging', ctx=Load()),
                                        attr='INFO',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Starting %s ...', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='getDescription',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='test', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='test',
                                        value=Name(id='test', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='time_start',
                                    ctx=Store(),
                                ),
                            ],
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='queries_start',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='sql_db', ctx=Load()),
                                attr='sql_counter',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='addError',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='test', annotation=None, type_comment=None),
                            arg(arg='err', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='addError',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='test', ctx=Load()),
                                    Name(id='err', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='logError',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='ERROR', kind=None),
                                    Name(id='test', ctx=Load()),
                                    Name(id='err', ctx=Load()),
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
                    name='addFailure',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='test', annotation=None, type_comment=None),
                            arg(arg='err', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='addFailure',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='test', ctx=Load()),
                                    Name(id='err', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='logError',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='FAIL', kind=None),
                                    Name(id='test', ctx=Load()),
                                    Name(id='err', ctx=Load()),
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
                    name='addSubTest',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='test', annotation=None, type_comment=None),
                            arg(arg='subtest', annotation=None, type_comment=None),
                            arg(arg='err', annotation=None, type_comment=None),
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
                                left=Name(id='err', ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='issubclass', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='err', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='test', ctx=Load()),
                                                attr='failureException',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='flavour', ctx=Store())],
                                            value=Constant(value='FAIL', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='flavour', ctx=Store())],
                                            value=Constant(value='ERROR', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='logError',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='flavour', ctx=Load()),
                                            Name(id='subtest', ctx=Load()),
                                            Name(id='err', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='addSubTest',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='test', ctx=Load()),
                                    Name(id='subtest', ctx=Load()),
                                    Name(id='err', ctx=Load()),
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
                    name='addSkip',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='test', annotation=None, type_comment=None),
                            arg(arg='reason', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='addSkip',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='test', ctx=Load()),
                                    Name(id='reason', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='log',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='logging', ctx=Load()),
                                        attr='INFO',
                                        ctx=Load(),
                                    ),
                                    Constant(value='skipped %s', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='getDescription',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='test', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='test',
                                        value=Name(id='test', ctx=Load()),
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
                    name='addUnexpectedSuccess',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='test', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='addUnexpectedSuccess',
                                    ctx=Load(),
                                ),
                                args=[Name(id='test', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='log',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='logging', ctx=Load()),
                                        attr='ERROR',
                                        ctx=Load(),
                                    ),
                                    Constant(value='unexpected success for %s', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='getDescription',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='test', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='test',
                                        value=Name(id='test', ctx=Load()),
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
                    name='logError',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='flavour', annotation=None, type_comment=None),
                            arg(arg='test', annotation=None, type_comment=None),
                            arg(arg='error', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='err', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_exc_info_to_string',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='error', ctx=Load()),
                                    Name(id='test', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='caller_infos', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='getErrorCallerInfo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='error', ctx=Load()),
                                    Name(id='test', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='log',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='logging', ctx=Load()),
                                        attr='INFO',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='=', kind=None),
                                        op=Mult(),
                                        right=Constant(value=70, kind=None),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='test',
                                        value=Name(id='test', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='caller_infos',
                                        value=Name(id='caller_infos', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='log',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='logging', ctx=Load()),
                                        attr='ERROR',
                                        ctx=Load(),
                                    ),
                                    Constant(value='%s: %s\n%s', kind=None),
                                    Name(id='flavour', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='getDescription',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='test', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Name(id='err', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='test',
                                        value=Name(id='test', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='caller_infos',
                                        value=Name(id='caller_infos', ctx=Load()),
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
                    name='getErrorCallerInfo',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='error', annotation=None, type_comment=None),
                            arg(arg='test', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        :param error: A tuple (exctype, value, tb) as returned by sys.exc_info().\n        :param test: A TestCase that created this error.\n        :returns: a tuple (fn, lno, func, sinfo) matching the logger findCaller format or None\n        ', kind=None),
                        ),
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='test', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='unittest', ctx=Load()),
                                            attr='suite',
                                            ctx=Load(),
                                        ),
                                        attr='_ErrorHolder',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='isinstance', ctx=Load()),
                                    args=[
                                        Name(id='test', ctx=Load()),
                                        Attribute(
                                            value=Name(id='unittest', ctx=Load()),
                                            attr='TestCase',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='%r is not a TestCase', kind=None),
                                                op=Mod(),
                                                right=Name(id='test', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(value=None),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='_', ctx=Store()),
                                        Name(id='_', ctx=Store()),
                                        Name(id='error_traceback', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='error', ctx=Load()),
                            type_comment=None,
                        ),
                        While(
                            test=Name(id='error_traceback', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='code', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='error_traceback', ctx=Load()),
                                            attr='tb_frame',
                                            ctx=Load(),
                                        ),
                                        attr='f_code',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='co_name',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='test', ctx=Load()),
                                                attr='_testMethodName',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='lineno', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='error_traceback', ctx=Load()),
                                                attr='tb_lineno',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='filename', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='code', ctx=Load()),
                                                attr='co_filename',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='method', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='test', ctx=Load()),
                                                attr='_testMethodName',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='infos', ctx=Store())],
                                            value=Tuple(
                                                elts=[
                                                    Name(id='filename', ctx=Load()),
                                                    Name(id='lineno', ctx=Load()),
                                                    Name(id='method', ctx=Load()),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Return(
                                            value=Name(id='infos', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='error_traceback', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='error_traceback', ctx=Load()),
                                        attr='tb_next',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
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
